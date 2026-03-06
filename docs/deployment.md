# Nanobot Deployment Guide

Nanobot is designed to be extremely lightweight, making it ideal for deployment on a wide range of hardware.

## Prerequisites
- Python ≥ 3.11
- At least 128MB RAM
- 50MB Disk space

## Deployment Targets

### 1. Local Development (macOS/Linux/Windows)
Simply clone and install in a virtual environment.
```bash
git clone https://github.com/mk-knight23/AI-Agent-Nanobot.git
cd AI-Agent-Nanobot
python -m venv venv
source venv/bin/activate
pip install -e .
```

### 2. Raspberry Pi Zero (SBC)
Nanobot is optimized for low-power ARM devices.
- Install `miniconda` or `miniforge` for ARMv6/v7.
- Use the `memory-optimization` workflow to tune RAM usage.
- Recommended to run as a `systemd` service.

### 3. Cloud (Vercel/DigitalOcean/Heroku)
Use the included `Dockerfile` for easy containerized deployment.
- Set API keys as Environment Variables.
- Enable `HEARTBEAT_LOGGING` for remote health monitoring.

## Configuration
Edit `config.json` to define your primary model and active channels.
```json
{
  "model": "claude-3-sonnet-20240229",
  "channels": ["telegram", "discord"],
  "skills_dir": "./skills"
}
```
