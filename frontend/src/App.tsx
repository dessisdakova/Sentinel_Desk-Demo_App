import { Navigate, Route, Routes } from "react-router-dom";

import { AuthProvider } from "@/auth/AuthContext";
import { AppLayout } from "@/components/AppLayout";
import { AuthNavigationGuard } from "@/components/AuthNavigationGuard";
import { ProtectedRoute } from "@/components/ProtectedRoute";
import { DashboardPage } from "@/pages/DashboardPage";
import { LoginPage } from "@/pages/LoginPage";

export function App() {
  return (
    <AuthProvider>
      <AuthNavigationGuard />
      <Routes>
        <Route path="/login" element={<LoginPage />} />
        <Route element={<ProtectedRoute />}>
          <Route element={<AppLayout />}>
            <Route index element={<Navigate to="/dashboard" replace />} />
            <Route path="/dashboard" element={<DashboardPage />} />
          </Route>
        </Route>
        <Route path="*" element={<Navigate to="/dashboard" replace />} />
      </Routes>
    </AuthProvider>
  );
}
