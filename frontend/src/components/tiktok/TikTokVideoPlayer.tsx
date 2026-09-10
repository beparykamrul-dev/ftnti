"use client";

import { useEffect, useRef } from "react";
import videojs, { type VideoJsPlayer } from "video.js";
import "video.js/dist/video-js.css";
import "@videojs/http-streaming";

export type TikTokVideoPlayerProps = {
  src: string;
  type?: "application/x-mpegURL" | "video/mp4";
  poster?: string;
  muted?: boolean;
};

export default function TikTokVideoPlayer({
  src,
  type = "application/x-mpegURL",
  poster,
  muted = true,
}: TikTokVideoPlayerProps) {
  const videoRef = useRef<HTMLVideoElement | null>(null);
  const playerRef = useRef<VideoJsPlayer | null>(null);

  useEffect(() => {
    if (!videoRef.current) return;

    playerRef.current = videojs(videoRef.current, {
      controls: true,
      responsive: true,
      fluid: true,
      muted,
      poster,
      sources: [{ src, type }],
      html5: {
        vhs: {
          overrideNative: false,
        },
      },
    });

    return () => {
      playerRef.current?.dispose();
      playerRef.current = null;
    };
  }, [muted, poster, src, type]);

  return (
    <div data-ftn-tiktok-player>
      <video ref={videoRef} className="video-js vjs-default-skin" playsInline />
    </div>
  );
}
