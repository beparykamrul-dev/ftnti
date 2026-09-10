import hashlib
import hmac
import os
import time


class TikTokSignatureError(ValueError):
    pass


def verify_tiktok_signature(raw_body: bytes, signature_header: str, max_age_seconds: int = 300) -> bool:
    secret = os.environ.get("TIKTOK_CLIENT_SECRET")
    if not secret:
        raise TikTokSignatureError("TikTok client secret is not configured")

    values = {}
    for part in signature_header.split(","):
        key, sep, value = part.strip().partition("=")
        if sep and key in {"t", "s"}:
            values[key] = value

    timestamp = values.get("t")
    provided = values.get("s")
    if not timestamp or not provided:
        raise TikTokSignatureError("Invalid TikTok signature header")

    try:
        timestamp_int = int(timestamp)
    except ValueError as exc:
        raise TikTokSignatureError("Invalid TikTok signature timestamp") from exc

    if abs(int(time.time()) - timestamp_int) > max_age_seconds:
        raise TikTokSignatureError("Expired TikTok webhook signature")

    signed_payload = f"{timestamp}.".encode() + raw_body
    expected = hmac.new(
        secret.encode(), signed_payload, hashlib.sha256
    ).hexdigest()

    if not hmac.compare_digest(expected, provided):
        raise TikTokSignatureError("Invalid TikTok webhook signature")

    return True
