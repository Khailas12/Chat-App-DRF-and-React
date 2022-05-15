from rest_framework import serializers
from .models import UserProfile, CustomUser
from message.serializers import GenericFileUploadSerializer


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        

class UserProfileSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    profile_pic = GenericFileUploadSerializer(read_only=True)
    profile_pic_id = serializers.IntegerField(write_only=True, required=False)
    
    class Meta:
        model = UserProfile
        fields = '__all__'