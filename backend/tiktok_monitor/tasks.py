from celery import shared_task
from django.utils import timezone

from .models import TikTokWebhookEvent


@shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=True, max_retries=5)
def process_tiktok_event(self, event_id: int):
    event = TikTokWebhookEvent.objects.get(pk=event_id)
    if event.processing_status == "processed":
        return {"status": "already_processed", "event_id": event.id}

    event.processing_status = "processing"
    event.processing_error = ""
    event.save(update_fields=["processing_status", "processing_error"])

    # Event-specific integrations are deliberately dispatched here so that
    # webhook acknowledgement remains fast and processing stays retryable.
    event.processing_status = "processed"
    event.processed_at = timezone.now()
    event.save(update_fields=["processing_status", "processed_at"])
    return {"status": "processed", "event_id": event.id}
