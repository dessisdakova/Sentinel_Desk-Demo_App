import { Outlet } from "react-router-dom";

import { AppNav } from "@/components/AppNav";

export function AppLayout() {
  return (
    <div className="min-h-screen bg-slate-950" data-testid="page-app-shell">
      <AppNav />
      <main className="mx-auto max-w-6xl px-6 py-8">
        <Outlet />
      </main>
    </div>
  );
}
