[![Deploy Next.js site to Pages](https://github.com/ezekiel-oss/ezee-ci-/actions/workflows/nextjs.yml/badge.svg)](https://github.com/ezekiel-oss/ezee-ci-/actions/workflows/nextjs.yml)

# Thesys AI — Repo Setup and Deployment

This repo contains your template zip (`template-c1-next.zip`). I’ve added helper scripts and project hygiene to quickly arrange the template so the app lives at the repo root, which is the best option for CI/CD and deployment.

## Quick Start (promote to repo root)

1) Extract and promote to root:
   - Run: `python3 scripts/extract_template.py --promote-to-root`
   - The script flattens the zip contents. If the zip has a single top-level folder, its contents are moved up.
   - Conflict handling:
     - If a `README.md` already exists, it’s backed up to `README.repo.md` and the template’s README becomes the root README.
     - If a `.gitignore` exists, the template’s one is saved as `.gitignore.template` and the current `.gitignore` is kept.
     - Other file conflicts will be saved with `.incoming` suffix.

2) Install and run (Next.js workflow assumed):
   - `npm install`
   - Development: `npm run dev`
   - Production build: `npm run build`
   - Start: `npm start` (or deploy via Vercel or your chosen platform)

## Integrate with thesysdev/template-c1-component-next

If you want to base your app on the official Thesys C1 component template, use the integration script:

- Run: `python3 scripts/integrate_thesys_component_next.py --promote-to-root`
  - Downloads the repo archive from GitHub.
  - Extracts and moves its contents to the repo root.
  - Backs up conflicting files (`README.repo.md`, `.gitignore.template`, `*.incoming`).
- After integration:
  - Set `THESYS_API_KEY` in your environment (or Vercel Project Settings → Environment Variables).
  - `npm install && npm run dev` to run locally.

## Vercel Deployment

You have two options:

- Git integration (recommended):
  1) Push this repo to GitHub/GitLab/Bitbucket.
  2) In Vercel, “Add New Project” → import this repo.
  3) Set environment variables in Project Settings → Environment Variables (use `.env.example` as a reference for keys; include `THESYS_API_KEY`).
  4) Vercel will auto-build and deploy on push.

- CI-driven deploy with Vercel CLI:
  1) Ensure the repo is linked to a Vercel project.
  2) Provide these CI env variables: `VERCEL_TOKEN`, `VERCEL_ORG_ID`, `VERCEL_PROJECT_ID`, and optionally `VERCEL_ENV` (`production` or `preview`).
  3) Run: `bash scripts/deploy_vercel.sh` in CI to build and deploy via CLI.
     - The script runs `vercel pull`, `vercel build`, and `vercel deploy --prebuilt`.

## GitHub Pages Deployment (via Actions)

- Workflow badge above points to the GitHub Actions workflow that builds and deploys to GitHub Pages.
- The workflow will:
  - Extract the template if not yet committed (uses `scripts/extract_template.py`),
  - Install dependencies, build, and run `next export`,
  - Upload the `out/` directory and deploy it to Pages.

## CI/CD (ezee-ci)

- Typical pipeline steps:
  - Install: `npm ci` (or `npm install` if no lockfile)
  - Lint/tests: `npm run lint && npm test` (if present)
  - Build: `npm run build`
  - Deploy:
    - Either rely on Vercel Git integration (no deploy step needed),
    - Or call `bash scripts/deploy_vercel.sh` with the required Vercel env variables.

## Notes

- `.gitignore` is added to keep Node/Next.js build artifacts out of version control.
- Add non-secret defaults to `.env.example`; set actual secrets in Vercel Project Settings.