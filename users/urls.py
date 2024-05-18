from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from .views import FriendRequestViewSet, FriendshipViewSet


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'friend_requests', FriendRequestViewSet)
router.register(r'friendships', FriendshipViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
