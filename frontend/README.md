# FTN TikTok frontend integrations

This package contains the browser-facing integration layer for the FTN TikTok module.

Included dependency groups:

- TikTok Shop Widget Kit / React Widget Kit
- TikTok Open API client
- Video.js + HLS.js playback primitives
- Socket.IO client for live UI transport where the backend exposes Socket.IO

## Important integration boundaries

- TikTok Pixel is intentionally **not** hard-coded into the repository as a tracking ID. Configure the pixel ID at deployment/runtime and obtain required consent before loading analytics/tracking code.
- Embed Videos and Green Screen Kit are represented by integration adapters/components rather than scraping or unofficial endpoints.
- TikTok Business SDK is an optional server-side integration. It is not placed in the browser bundle because business credentials and access tokens must remain server-side.
- `videojs/http-streaming` is provided by the Video.js HTTP Streaming package in modern Video.js distributions; do not assume a separate browser package is required without verifying the installed Video.js version.

## Install

```bash
npm install
```

## Build

```bash
npm run build
```
