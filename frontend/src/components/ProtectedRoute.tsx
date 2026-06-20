import { Navigate, Outlet } from "react-router-dom";

import { useAuth } from "@/auth/AuthContext";

export function ProtectedRoute() {
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

  if (!isAuthenticated) {
    return <Navigate to="/login" replace />;
  }

  return <Outlet />;
}
