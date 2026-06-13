import type { UserRole } from "@/types/auth";

export interface NavItem {
  label: string;
  path: string;
  testId: string;
  roles: UserRole[];
  disabled: boolean;
}

export const NAV_ITEMS: NavItem[] = [
  {
    label: "Dashboard",
    path: "/dashboard",
    testId: "nav-dashboard",
    roles: ["ANALYST", "LEAD", "ADMIN"],
    disabled: true,
  },
  {
    label: "Alerts",
    path: "/alerts",
    testId: "nav-alerts",
    roles: ["ANALYST", "LEAD", "ADMIN"],
    disabled: true,
  },
  {
    label: "Cases",
    path: "/cases",
    testId: "nav-cases",
    roles: ["ANALYST", "LEAD", "ADMIN"],
    disabled: true,
  },
  {
    label: "Playbooks",
    path: "/playbooks",
    testId: "nav-playbooks",
    roles: ["ANALYST", "LEAD", "ADMIN"],
    disabled: true,
  },
  {
    label: "Audit",
    path: "/audit",
    testId: "nav-audit",
    roles: ["LEAD", "ADMIN"],
    disabled: true,
  },
  {
    label: "Admin",
    path: "/admin",
    testId: "nav-admin",
    roles: ["ADMIN"],
    disabled: true,
  },
];

export function navItemsForRole(role: UserRole): NavItem[] {
  return NAV_ITEMS.filter((item) => item.roles.includes(role));
}
