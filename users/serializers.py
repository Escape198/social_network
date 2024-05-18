from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import FriendRequest, Friendship


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'bio', 'profile_picture')


class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = ('id', 'sender', 'receiver', 'status', 'created_at')


class FriendshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friendship
        fields = ('id', 'user1', 'user2', 'created_at')
