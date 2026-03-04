/**
 * Centralized configuration for the application.
 * Uses environment variables with sensible defaults for development.
 */

export const API_BASE = (import.meta as any).env?.VITE_API_BASE_URL || "http://localhost:8000/api/v1";

export const APP_CONFIG = {
  API_BASE,
  isProduction: (import.meta as any).env?.PROD ?? false,
};
