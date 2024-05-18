from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import VerificationRequest
from .serializers import VerificationRequestSerializer


class VerificationRequestViewSet(viewsets.ModelViewSet):
    queryset = VerificationRequest.objects.all()
    serializer_class = VerificationRequestSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)