# models.py
import uuid
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# class QRAuthSession(models.Model):
#     session_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
#     user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
#     is_authenticated = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     expires_at = models.DateTimeField()

#     def is_expired(self):
#         return timezone.now() > self.expires_at

#     def __str__(self):
#         return str(self.session_id)

class TemporaryId(models.Model):
    temp_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_expired(self, minutes=2):
        return timezone.now() > self.created_at + timezone.timedelta(minutes=minutes)

    def __str__(self):
        return str(self.temp_id)

class QRAuthSession(models.Model):
    session_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    is_authenticated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    
    def is_expired(self):
        return timezone.now() > self.expires_at

    def __str__(self):
        return str(self.session_id)

