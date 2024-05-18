from django.urls import path, include


urlpatterns = [
    path('users/', include('users.urls')),
    path('posts/', include('posts.urls')),
    path('messages/', include('messages.urls')),
    path('notifications/', include('notifications.urls')),
    path('search/', include('search.urls')),
    path('groups/', include('groups.urls')),
    path('events/', include('events.urls')),
    path('gallery/', include('gallery.urls')),
    path('marketplace/', include('marketplace.urls')),
    path('verification/', include('verification.urls')),
]
