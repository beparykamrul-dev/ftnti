from django.db import models


class TikTokAccount(models.Model):
    ftn_user_id = models.CharField(max_length=128, db_index=True)
    open_id = models.CharField(max_length=255, unique=True)
    display_name = models.CharField(max_length=255, blank=True)
    scopes = models.JSONField(default=list, blank=True)
    token_expires_at = models.DateTimeField(null=True, blank=True)
    refresh_token_expires_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=32, default="active", db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.display_name or self.open_id


class TikTokWebhookEvent(models.Model):
    idempotency_key = models.CharField(max_length=512, unique=True)
    client_key = models.CharField(max_length=255, db_index=True)
    event_type = models.CharField(max_length=128, db_index=True)
    create_time = models.BigIntegerField(null=True, blank=True)
    user_openid = models.CharField(max_length=255, blank=True, db_index=True)
    content = models.JSONField(default=dict, blank=True)
    raw_payload = models.JSONField(default=dict, blank=True)
    received_at = models.DateTimeField(auto_now_add=True)
    processed_at = models.DateTimeField(null=True, blank=True)
    processing_status = models.CharField(max_length=32, default="pending", db_index=True)
    processing_error = models.TextField(blank=True)

    class Meta:
        indexes = [
            models.Index(fields=["event_type", "received_at"]),
            models.Index(fields=["processing_status", "received_at"]),
        ]

    def __str__(self):
        return f"{self.event_type}:{self.idempotency_key}"
