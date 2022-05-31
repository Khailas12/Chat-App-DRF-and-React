from . import models, serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated



class UserProfileView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = models.UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer