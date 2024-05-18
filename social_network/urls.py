from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/posts/', include('posts.urls')),
    path('api/messages/', include('messages.urls')),
    path('api/notifications/', include('notifications.urls')),
    path('api/search/', include('search.urls')),
    path('api/groups/', include('groups.urls')),
    path('api/events/', include('events.urls')),
    path('api/gallery/', include('gallery.urls')),
    path('api/marketplace/', include('marketplace.urls')),
    path('api/verification/', include('verification.urls')),
    path('api/', include('api.urls')),
]
