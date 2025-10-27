# Thesys AI — Repo Setup and Deployment

This repo contains your template zip (`template-c1-next.zip`). The best arrangement for deployment is to extract the template into a working application directory and run it as the root app or a clear sub-app. I’ve added a helper script and basic project hygiene so you can proceed quickly.

## Quick Start

1) Extract the template into a folder named `thesys-ai`:
   - Run: `python3 scripts/extract_template.py`
   - This will produce: `./thesys-ai/` with the template contents properly flattened (it handles zips that contain a single top-level folder).

2) Install and run (Next.js workflow assumed):
   - `cd thesys-ai`
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
- If you prefer the template as the repo root (not in `thesys-ai`), let me know and I’ll re-arrange the files after extraction.
- If your template needs specific environment variables (e.g., for “Thesys AI”), add them in a `.env.local` for local dev and configure them in ezee-ci for builds.