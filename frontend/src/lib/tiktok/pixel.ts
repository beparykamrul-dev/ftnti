"use client";

import TiktokPixel from "tiktok-pixel";

let initialized = false;

export function initTikTokPixel(pixelId?: string) {
  if (!pixelId || initialized) return false;
  TiktokPixel.init(pixelId, undefined, { debug: false });
  initialized = true;
  return true;
}

export function trackTikTokPageView() {
  if (initialized) TiktokPixel.pageView();
}

export function trackTikTokEvent(
  event: string,
  data?: Record<string, unknown>,
  eventId?: string,
) {
  if (!initialized) return false;
  TiktokPixel.track(event, data, eventId ? { event_id: eventId } : undefined);
  return true;
}
