from rest_framework import serializers
from .models import UserProfile, CustomUser
from message.serializers import GenericFileUploadSerializer

from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'id',
            'first_name',
            'last_name',
            'username',
        ]

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True, 
        validators=[UniqueValidator(queryset=UserProfile.objects.all())]
    )
    
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = UserProfile
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
            'password2',
        ]
        extra_kwargs = {
            'first_name' : {'required': True},
            'last_name' : {'required': True}
        }
        
    def validata(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {'password': 'Password Does not match'}
            )
        return attrs
    
    
    def create(self, validatad_data):
        user = UserProfile.objects.create(
            first_name = validatad_data['first_name'],
            last_name = validatad_data['last_name'],
            username = validatad_data['username'],
            email = validatad_data['email'],
            password = validatad_data['password'],
            password2 = validatad_data['password2'],
        )
        
        user.set_password(validatad_data['password'])
        user.save()
        return user
    

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