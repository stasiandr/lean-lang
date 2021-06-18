from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from django.contrib.auth import get_user_model  # If used custom user model
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import UserSerializer
from .serializers import CustomTokenObtainPairSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    # Replace the serializer with your custom
    serializer_class = CustomTokenObtainPairSerializer


class CreateUserView(ListCreateAPIView):
    model = get_user_model()

    queryset = model.objects

    permission_classes = [
        permissions.AllowAny  # Or anon users can't register
    ]
    serializer_class = UserSerializer


class RetrieveUserView(RetrieveAPIView):
    model = get_user_model()

    queryset = model.objects

    permission_classes = [
        permissions.IsAuthenticated
#      permissions.AllowAny  # Or anon users can't register
    ]
    serializer_class = UserSerializer
