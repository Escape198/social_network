from django.db import models
from django.contrib.auth import get_user_model


class VerificationRequest(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='verification_requests')
    document = models.FileField(upload_to='verification_documents/')
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Verification request for {self.user} with status {self.status}"
