from .models import CustomUser
from rest_framework import serializers
from django.contrib.auth import get_user_model  # If used custom user model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

UserModel = get_user_model()


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        data.update({'id': self.user.id})
        return data


# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        return UserModel.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )

    class Meta:
        model = UserModel
        fields = ['id', 'email', 'password', "first_name", "last_name", "role"]
