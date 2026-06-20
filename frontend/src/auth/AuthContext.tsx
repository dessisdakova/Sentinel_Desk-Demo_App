import {
  createContext,
  useCallback,
  useContext,
  useEffect,
  useMemo,
  useState,
  type ReactNode,
} from "react";

import { apiRequest, configureApiClient, TOKEN_STORAGE_KEY } from "@/api/client";
import type { TokenResponse, UserProfile } from "@/types/auth";

interface AuthContextValue {
  token: string | null;
  user: UserProfile | null;
  isAuthenticated: boolean;
  isLoading: boolean;
  login: (email: string, password: string) => Promise<void>;
  logout: () => Promise<void>;
}

const AuthContext = createContext<AuthContextValue | null>(null);

function readStoredToken(): string | null {
  return sessionStorage.getItem(TOKEN_STORAGE_KEY);
}

function persistToken(token: string | null): void {
  if (token) {
    sessionStorage.setItem(TOKEN_STORAGE_KEY, token);
  } else {
    sessionStorage.removeItem(TOKEN_STORAGE_KEY);
  }
}

interface AuthProviderProps {
  children: ReactNode;
}

export function AuthProvider({ children }: AuthProviderProps) {
  const [token, setToken] = useState<string | null>(() => readStoredToken());
  const [user, setUser] = useState<UserProfile | null>(null);
  const [isLoading, setIsLoading] = useState<boolean>(() => readStoredToken() !== null);

  const clearSession = useCallback(() => {
    setToken(null);
    setUser(null);
    persistToken(null);
  }, []);

  const loadProfile = useCallback(async (activeToken: string) => {
    const profile = await apiRequest<UserProfile>("/api/v1/auth/me", {
      headers: {
        Authorization: `Bearer ${activeToken}`,
      },
    });
    setUser(profile);
  }, []);

  useEffect(() => {
    configureApiClient(
      () => token,
      () => {
        clearSession();
      },
    );
  }, [token, clearSession]);

  useEffect(() => {
    const storedToken = readStoredToken();
    if (!storedToken) {
      setIsLoading(false);
      return;
    }

    let cancelled = false;

    const bootstrap = async () => {
      setIsLoading(true);
      try {
        await loadProfile(storedToken);
        if (!cancelled) {
          setToken(storedToken);
        }
      } catch {
        if (!cancelled) {
          clearSession();
        }
      } finally {
        if (!cancelled) {
          setIsLoading(false);
        }
      }
    };

    void bootstrap();

    return () => {
      cancelled = true;
    };
  }, [clearSession, loadProfile]);

  const login = useCallback(
    async (email: string, password: string) => {
      const response = await apiRequest<TokenResponse>("/api/v1/auth/login", {
        method: "POST",
        body: JSON.stringify({ email, password }),
      });

      persistToken(response.access_token);
      setToken(response.access_token);
      await loadProfile(response.access_token);
    },
    [loadProfile],
  );

  const logout = useCallback(async () => {
    if (token) {
      try {
        await apiRequest<void>("/api/v1/auth/logout", { method: "POST" });
      } catch {
        // Client-side session is cleared even when the API call fails.
      }
    }
    clearSession();
  }, [clearSession, token]);

  const value = useMemo<AuthContextValue>(
    () => ({
      token,
      user,
      isAuthenticated: token !== null && user !== null,
      isLoading,
      login,
      logout,
    }),
    [token, user, isLoading, login, logout],
  );

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

export function useAuth(): AuthContextValue {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error("useAuth must be used within AuthProvider");
  }
  return context;
}
