import { NavLink } from "react-router-dom";

import { useAuth } from "@/auth/AuthContext";
import { navItemsForRole } from "@/config/navigation";

export function AppNav() {
  const { user, logout } = useAuth();

  if (!user) {
    return null;
  }

  const items = navItemsForRole(user.role);

  return (
    <header className="border-b border-slate-800 bg-slate-900">
      <div className="mx-auto flex max-w-6xl items-center justify-between gap-6 px-6 py-4">
        <div className="flex items-center gap-8">
          <span className="text-lg font-semibold text-slate-100">SentinelDesk</span>
          <nav className="flex items-center gap-2" data-testid="app-nav">
            {items.map((item) =>
              item.disabled ? (
                <span
                  key={item.path}
                  aria-disabled="true"
                  className="cursor-not-allowed rounded-md px-3 py-2 text-sm text-slate-500"
                  data-testid={item.testId}
                >
                  {item.label}
                </span>
              ) : (
                <NavLink
                  key={item.path}
                  to={item.path}
                  className={({ isActive }) =>
                    [
                      "rounded-md px-3 py-2 text-sm transition-colors",
                      isActive
                        ? "bg-slate-800 text-white"
                        : "text-slate-300 hover:bg-slate-800 hover:text-white",
                    ].join(" ")
                  }
                  data-testid={item.testId}
                >
                  {item.label}
                </NavLink>
              ),
            )}
          </nav>
        </div>
        <div className="flex items-center gap-4">
          <span className="text-sm text-slate-400" data-testid="nav-user-email">
            {user.display_name} ({user.role})
          </span>
          <button
            type="button"
            onClick={() => {
              void logout();
            }}
            className="rounded-md border border-slate-700 px-3 py-2 text-sm text-slate-200 transition-colors hover:bg-slate-800"
            data-testid="nav-logout"
          >
            Log out
          </button>
        </div>
      </div>
    </header>
  );
}
