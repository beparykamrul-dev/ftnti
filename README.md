# FTN Unified Platform

Family Time Network (FTN) unified ISP platform.

## Scope

This repository is the central production codebase for the FTN control plane and supporting services:

- Django API/control plane
- TikTok webhook/event ingestion
- Celery + Redis asynchronous processing
- Django Channels/WebSocket live updates
- PostgreSQL data layer
- ISP traffic ingestion and customer-level accounting integration
- MikroTik/PPPoE session mapping integration points
- Nginx production reverse proxy
- systemd/Docker deployment assets
- health, readiness and audit foundations

## Repository layout

```text
ftnti/
├── backend/                 # Django control plane
│   ├── config/              # Django/ASGI/Celery configuration
│   ├── tiktok_monitor/      # Webhook and event processing
│   └── traffic/             # ISP traffic/accounting domain
├── deploy/
│   ├── nginx/
│   └── systemd/
├── docker/
├── scripts/
├── .env.example
├── docker-compose.yml
└── requirements.txt
```

## Security principles

- Secrets are environment-only and are never committed.
- TikTok webhook signatures are verified before processing.
- Webhook processing is idempotent.
- Public application traffic terminates at HTTPS/Nginx; internal Django ports are not intended for public exposure.
- Customer traffic accounting is based on authenticated network/session mappings, not TikTok API data.

## Production status

The repository starts as the canonical FTN platform foundation. Existing server-side code under `/opt/ftn/backend` must be reconciled into this repository before claiming that every currently deployed feature has been migrated.
