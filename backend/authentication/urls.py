from django.urls import path, include
from rest_framework import routers

from authentication import views
from authentication.views import CreateUserView, RetrieveUserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)

router = routers.DefaultRouter()
# router.register(r'users/', CreateUserView, basename="User")

urlpatterns = [
    path('users/<int:pk>/', RetrieveUserView.as_view()),
    path(r'users/', CreateUserView.as_view()),
    path(r'token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(r'token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path(r'token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
