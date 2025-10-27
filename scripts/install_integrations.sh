#!/usr/bin/env bash
set -euo pipefail

# Integrate the Thesys component template or local zip into repo root if package.json is missing,
# then install dependencies. Designed for Vercel installCommand.

if [ -f package.json ]; then
  echo "package.json present; skipping integration."
else
  echo "No package.json found; attempting integration."

  # Prefer integrating thesysdev/template-c1-component-next
  if command -v python3 >/dev/null 2>&1 && [ -f scripts/integrate_thesys_component_next.py ]; then
    echo "Running integrate_thesys_component_next.py"
    python3 scripts/integrate_thesys_component_next.py --promote-to-root || true
  fi

  # Fallback to local zip extraction if still missing
  if [ ! -f package.json ] && [ -f scripts/extract_template.py ] && [ -f template-c1-next.zip ]; then
    if command -v python3 >/dev/null 2>&1; then
      echo "Extracting template-c1-next.zip"
      python3 scripts/extract_template.py --promote-to-root || true
    fi
  fi

  if [ ! -f package.json ]; then
    echo "Integration did not produce package.json; continuing to install step."
  fi
fi

echo "Installing dependencies"
if [ -f package-lock.json ]; then
  npm ci || npm install
else
  npm install
fi