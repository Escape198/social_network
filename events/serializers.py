from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name', 'description', 'location', 'start_time', 'end_time', 'created_by', 'attendees', 'created_at', 'updated_at')
