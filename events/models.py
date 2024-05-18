from django.db import models
from django.contrib.auth import get_user_model


class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='created_events')
    attendees = models.ManyToManyField(get_user_model(), related_name='events')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
