from django.db import models
from django.contrib.auth import get_user_model


class Image(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image uploaded by {self.user} at {self.uploaded_at}"
