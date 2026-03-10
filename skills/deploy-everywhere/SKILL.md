---
name: deploy-everywhere
description: "Deploy a Python AI agent or app to multiple platforms in one command: Railway, Fly.io, Docker Hub, AWS Lambda, and GitHub Actions CI. Generates Dockerfile, platform-specific configs, environment variable templates, and a deployment checklist. Adapted from OpenClaw's multi-platform deployment pipeline. Use when you want to ship Nanobot-powered tools to production without manual config per platform."
---

# deploy-everywhere

Ship your Nanobot app to 10 platforms from one command.

## Usage
```
@Nanobot deploy-everywhere --platforms railway,fly,lambda
@Nanobot deploy-everywhere --platforms docker --push ghcr.io/mk-knight23/nanobot
@Nanobot deploy-everywhere --dry-run      # Preview all configs, don't deploy
@Nanobot deploy-everywhere --platform github-actions --trigger push:main
```

## Supported Platforms

| Platform | Config Generated | Deploy Method |
|----------|-----------------|---------------|
| Railway | `railway.toml` | `railway up` |
| Fly.io | `fly.toml` | `fly deploy` |
| AWS Lambda | `serverless.yml` | `sls deploy` |
| Docker Hub | `Dockerfile` | `docker push` |
| GitHub Actions | `.github/workflows/deploy.yml` | git push |
| Render | `render.yaml` | git push |
| Heroku | `Procfile` | `git push heroku` |

## Files Created
```
Dockerfile                          # Multi-stage Python build, <150MB image
.dockerignore                       # Excludes .env, __pycache__, tests
railway.toml                        # Railway service + env config
fly.toml                            # Fly.io app config
.github/workflows/deploy.yml        # CI/CD pipeline
.env.template                       # All required env vars (no secrets)
DEPLOY_CHECKLIST.md                 # Pre-flight checklist before going live
```

## What It Handles

### 1. Dependency Optimization
- Uses `uv` for fast Docker layer caching
- Separates production from dev deps
- Pins exact versions in `requirements.lock`

### 2. Environment Variable Management
- Scans code for `os.environ` and `os.getenv` calls
- Generates `.env.template` with all required vars
- Adds startup validation: fails fast if required vars are missing

### 3. Health Check Endpoint
- Injects `/health` endpoint into your agent gateway
- Returns: uptime, version, active provider, memory usage

### 4. Secrets Detection
- Blocks deploy if `.env` file is in git staging
- Warns on hardcoded strings matching secret patterns
- Integrates with `git-secrets` if installed

## Multi-Platform CI/CD
```yaml
# Generated .github/workflows/deploy.yml
on:
  push:
    branches: [main]
jobs:
  deploy:
    steps:
      - uses: actions/checkout@v4
      - run: pip install uv && uv sync
      - run: python -m pytest --tb=short
      - run: railway up          # or fly deploy, etc.
```

## Philosophy
Nanobot should ship everywhere. One Docker image, multiple runtimes. The skill handles the plumbing so you focus on the agent logic.
