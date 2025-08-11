from rest_framework import serializers
from .models import QRAuthSession, TemporaryId

class QRAuthSessionSerializer(serializers.ModelSerializer):
    model = QRAuthSession
    fields = ["session_id", 'user', 'is_authenticated', "created_at"]
    read_only_fields = ['user', 'is_authenticate', 'created_at']


class TemporaryIdSerializer(serializers.ModelSerializer):
    model = TemporaryId
    fields = ['temp_id', "created_at"]
