# Thesys AI — Repo Setup and Deployment

This repo contains your template zip (`template-c1-next.zip`). I’ve added a helper script and project hygiene to quickly arrange the template so the app lives at the repo root, which is the best option for CI/CD and deployment.

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

3) CI/CD (ezee-ci)
   - Typical pipeline steps:
     - Install: `npm ci`
     - Lint/tests: `npm run lint && npm test` (if present)
     - Build: `npm run build`
     - Deploy: either to Vercel (recommended for Next.js) or to your server/container.
   - Ensure environment variables (e.g., API keys, secrets) are configured in ezee-ci before build/deploy.

## Deployment Options

- Vercel (recommended for Next.js):
  - Connect the repo, set environment variables, and Vercel will build/deploy on push.
- Custom server / container:
  - Build in CI (`npm run build`) and deploy the `.next` output (with Node server), or containerize and roll out using your infra.
- Static export (if the template supports it):
  - `next build && next export` produces `out/` which can be deployed as static files.

## Notes

- `.gitignore` is added to keep Node/Next.js build artifacts out of version control.
- If your template needs specific environment variables (e.g., for “Thesys AI”), add them in a `.env.local` for local dev and configure them in ezee-ci for builds.