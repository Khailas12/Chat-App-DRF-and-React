from rest_framework import serializers
from .models import UserProfile, CustomUser
from message.serializers import GenericFileUploadSerializer

from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password



class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required = True,
        validators = [UniqueValidator(
            queryset=UserProfile.objects.all()
        )]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password_2=serializers.CharField(
        write_only=True, required=True
    )
    
    fields = (
        'first_name',
        'last_name'
        'username',
        'email',
        'password',
        'password_2',
        )
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password_2']:
            raise serializers.ValidationError({
                'password': 'Password does not match'
            })
        return attrs
    
    def create(self, validated_data):
        user = UserProfile.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name']
        )
    
        extra_kwargs = {
            'first_name' : {'required': True},
            'last_name' : {'required': True}
        }
        
        user.set_password(validated_data['password'])
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