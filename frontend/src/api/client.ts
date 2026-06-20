import type { ApiErrorBody } from "@/types/auth";

export const TOKEN_STORAGE_KEY = "sentinel_access_token";

const API_URL = import.meta.env.VITE_API_URL as string;

if (!API_URL) {
  throw new Error("VITE_API_URL is not defined");
}

export class ApiRequestError extends Error {
  readonly status: number;
  readonly code: string;
  readonly details: unknown;

  constructor(status: number, body: ApiErrorBody) {
    super(body.error.message);
    this.name = "ApiRequestError";
    this.status = status;
    this.code = body.error.code;
    this.details = body.error.details;
  }
}

type TokenGetter = () => string | null;
type UnauthorizedHandler = () => void;

let tokenGetter: TokenGetter = () => null;
let unauthorizedHandler: UnauthorizedHandler = () => undefined;

export function configureApiClient(
  getToken: TokenGetter,
  onUnauthorized: UnauthorizedHandler,
): void {
  tokenGetter = getToken;
  unauthorizedHandler = onUnauthorized;
}

async function parseErrorResponse(response: Response): Promise<ApiErrorBody> {
  try {
    const body = (await response.json()) as ApiErrorBody;
    if (body?.error?.message) {
      return body;
    }
  } catch {
    // Fall through to generic error envelope.
  }

  return {
    error: {
      code: "HTTP_ERROR",
      message: response.statusText || "Request failed",
      details: null,
    },
  };
}

export async function apiRequest<T>(
  path: string,
  init: RequestInit = {},
): Promise<T> {
  const headers = new Headers(init.headers);
  if (!headers.has("Content-Type") && init.body) {
    headers.set("Content-Type", "application/json");
  }

  const token = tokenGetter();
  if (token) {
    headers.set("Authorization", `Bearer ${token}`);
  }

  const response = await fetch(`${API_URL}${path}`, {
    ...init,
    headers,
  });

  if (response.status === 401 && !path.endsWith("/auth/login")) {
    unauthorizedHandler();
  }

  if (!response.ok) {
    const errorBody = await parseErrorResponse(response);
    throw new ApiRequestError(response.status, errorBody);
  }

  if (response.status === 204) {
    return undefined as T;
  }

  return (await response.json()) as T;
}
