export type UserRole = "ANALYST" | "LEAD" | "ADMIN";

export interface UserProfile {
  id: string;
  email: string;
  role: UserRole;
  display_name: string;
}

export interface TokenResponse {
  access_token: string;
  token_type: string;
  expires_in: number;
}

export interface ApiErrorBody {
  error: {
    code: string;
    message: string;
    details: unknown;
  };
}
