from rest_framework import serializers
from .models import VerificationRequest


class VerificationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerificationRequest
        fields = ('id', 'user', 'document', 'status', 'created_at', 'updated_at')
