import { zodResolver } from "@hookform/resolvers/zod";
import { useMutation } from "@tanstack/react-query";
import { useForm } from "react-hook-form";
import { Navigate, useNavigate } from "react-router-dom";

import { ApiRequestError } from "@/api/client";
import { useAuth } from "@/auth/AuthContext";
import { loginFormSchema, type LoginFormValues } from "@/schemas/login";

export function LoginPage() {
  const { login, isAuthenticated, isLoading } = useAuth();
  const navigate = useNavigate();

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<LoginFormValues>({
    resolver: zodResolver(loginFormSchema),
    defaultValues: {
      email: "",
      password: "",
    },
  });

  const loginMutation = useMutation({
    mutationFn: async (values: LoginFormValues) => {
      await login(values.email, values.password);
    },
    onSuccess: () => {
      navigate("/dashboard", { replace: true });
    },
  });

  const apiError =
    loginMutation.error instanceof ApiRequestError &&
    loginMutation.error.status === 401
      ? loginMutation.error.message
      : loginMutation.error instanceof ApiRequestError
        ? loginMutation.error.message
        : null;

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

  const onSubmit = (values: LoginFormValues) => {
    loginMutation.reset();
    loginMutation.mutate(values);
  };

  return (
    <div
      className="flex min-h-screen items-center justify-center bg-slate-950 px-6"
      data-testid="page-login"
    >
      <div className="w-full max-w-md rounded-lg border border-slate-800 bg-slate-900 p-8">
        <h1 className="text-center text-2xl font-semibold text-slate-100">
          SentinelDesk
        </h1>
        <p className="mt-2 text-center text-sm text-slate-400">
          Sign in to the SecOps Alert Triage Portal
        </p>

        <form
          className="mt-8 space-y-5"
          onSubmit={(event) => {
            void handleSubmit(onSubmit)(event);
          }}
          noValidate
        >
          {apiError ? (
            <div
              className="rounded-md border border-red-800 bg-red-950/50 px-4 py-3 text-sm text-red-200"
              data-testid="login-error"
              role="alert"
            >
              {apiError}
            </div>
          ) : null}

          <div>
            <label
              htmlFor="login-email-input"
              className="mb-1.5 block text-sm font-medium text-slate-300"
            >
              Email
            </label>
            <input
              id="login-email-input"
              type="email"
              autoComplete="email"
              className="w-full rounded-md border border-slate-700 bg-slate-950 px-3 py-2 text-slate-100 placeholder:text-slate-500 focus:border-slate-500 focus:outline-none focus:ring-1 focus:ring-slate-500"
              data-testid="login-email"
              {...register("email")}
            />
            {errors.email ? (
              <p className="mt-1.5 text-sm text-red-400">{errors.email.message}</p>
            ) : null}
          </div>

          <div>
            <label
              htmlFor="login-password-input"
              className="mb-1.5 block text-sm font-medium text-slate-300"
            >
              Password
            </label>
            <input
              id="login-password-input"
              type="password"
              autoComplete="current-password"
              className="w-full rounded-md border border-slate-700 bg-slate-950 px-3 py-2 text-slate-100 placeholder:text-slate-500 focus:border-slate-500 focus:outline-none focus:ring-1 focus:ring-slate-500"
              data-testid="login-password"
              {...register("password")}
            />
            {errors.password ? (
              <p className="mt-1.5 text-sm text-red-400">
                {errors.password.message}
              </p>
            ) : null}
          </div>

          <button
            type="submit"
            disabled={loginMutation.isPending}
            className="w-full rounded-md bg-sky-600 px-4 py-2.5 text-sm font-medium text-white transition-colors hover:bg-sky-500 disabled:cursor-not-allowed disabled:opacity-60"
            data-testid="login-submit"
          >
            {loginMutation.isPending ? "Signing in…" : "Sign in"}
          </button>
        </form>
      </div>
    </div>
  );
}
