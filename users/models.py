from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)


class FriendRequest(models.Model):
    sender = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='sent_friend_requests')
    receiver = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='received_friend_requests')
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)


class Friendship(models.Model):
    user1 = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='friends1')
    user2 = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='friends2')
    created_at = models.DateTimeField(auto_now_add=True)