import "server-only";

export type TikTokEmbedProps = {
  videoId: string;
  autoplay?: 0 | 1;
  loop?: 0 | 1;
  controls?: 0 | 1;
  description?: 0 | 1;
  musicInfo?: 0 | 1;
};

export function TikTokEmbed({
  videoId,
  autoplay = 0,
  loop = 0,
  controls = 1,
  description = 1,
  musicInfo = 1,
}: TikTokEmbedProps) {
  const query = new URLSearchParams({
    autoplay: String(autoplay),
    loop: String(loop),
    controls: String(controls),
    description: String(description),
    music_info: String(musicInfo),
  });

  return (
    <iframe
      title="TikTok video"
      src={`https://www.tiktok.com/player/v1/${encodeURIComponent(videoId)}?${query.toString()}`}
      style={{ width: "100%", aspectRatio: "9 / 16", border: 0 }}
      allow="fullscreen"
      loading="lazy"
    />
  );
}
