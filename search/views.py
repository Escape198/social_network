from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from posts.models import Post
from users.serializers import UserSerializer
from posts.serializers import PostSerializer


class SearchView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request, *args, **kwargs):
        query = request.query_params.get('q', '')
        user_results = get_user_model().objects.filter(username__icontains=query)
        post_results = Post.objects.filter(title__icontains=query)

        user_serializer = UserSerializer(user_results, many=True)
        post_serializer = PostSerializer(post_results, many=True)

        return Response({
            'users': user_serializer.data,
            'posts': post_serializer.data,
        })
