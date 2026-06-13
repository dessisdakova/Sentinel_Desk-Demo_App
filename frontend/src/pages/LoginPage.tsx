import { Navigate } from "react-router-dom";

import { useAuth } from "@/auth/AuthContext";

export function LoginPage() {
  const { isAuthenticated, isLoading } = useAuth();

  if (isLoading) {
    return (
      <div
        className="flex min-h-screen items-center justify-center bg-slate-950 text-slate-300"
        data-testid="auth-loading"
      >
        <p>Loading session…</p>
      </div>
    );
  }

  if (isAuthenticated) {
    return <Navigate to="/dashboard" replace />;
  }

  return (
    <div
      className="flex min-h-screen items-center justify-center bg-slate-950 px-6"
      data-testid="page-login-placeholder"
    >
      <div className="w-full max-w-md rounded-lg border border-slate-800 bg-slate-900 p-8 text-center">
        <h1 className="text-2xl font-semibold text-slate-100">SentinelDesk</h1>
        <p className="mt-4 text-sm text-slate-400">
          Login form ships in SENT-107. Use the auth API directly until then.
        </p>
      </div>
    </div>
  );
}
