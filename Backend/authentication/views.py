from httplib2 import Response
from . import models, serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework import generics


class UserProfileView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = models.UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer
    

class UserDetailAPI(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowAny)
    
    def get(self, request, *args, **kwargs):
        user = models.UserProfile.objects.get(id=request.user.id)
        serializer = serializers.UserSerializer(user)
        return Response(serializer.data)
    
    
class RegisterUserView(generics.CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = serializers.RegisterSerializer