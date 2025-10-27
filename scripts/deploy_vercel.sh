#!/usr/bin/env bash
set -euo pipefail

# Deploy to Vercel using the recommended CI flow:
# - Requires environment variables:
#   VERCEL_TOKEN       (Personal Token)
#   VERCEL_ORG_ID      (Organization ID)
#   VERCEL_PROJECT_ID  (Project ID)
#   VERCEL_ENV         (optional: "production" or "preview", default "production")
#
# This script will:
# 1) Pull env/config from Vercel
# 2) Build the project locally in CI
# 3) Deploy the prebuilt output to Vercel

ENV="${VERCEL_ENV:-production}"

if [[ -z "${VERCEL_TOKEN:-}" || -z "${VERCEL_ORG_ID:-}" || -z "${VERCEL_PROJECT_ID:-}" ]]; then
  echo "Missing required env: VERCEL_TOKEN, VERCEL_ORG_ID, VERCEL_PROJECT_ID" >&2
  exit 1
fi

echo "Pulling environment: $ENV"
npx vercel pull --yes --environment="$ENV" --token "$VERCEL_TOKEN"

echo "Building project"
npx vercel build --token "$VERCEL_TOKEN"

echo "Deploying prebuilt output"
if [[ "$ENV" == "production" ]]; then
  npx vercel deploy --prebuilt --prod --token "$VERCEL_TOKEN"
else
  npx vercel deploy --prebuilt --token "$VERCEL_TOKEN"
fi

echo "Deployment complete."