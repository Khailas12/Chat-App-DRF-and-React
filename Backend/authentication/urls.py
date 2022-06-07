from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView, TokenVerifyView
)


router = DefaultRouter(trailing_slash=False)
router.register('profile', views.UserProfileView)

urlpatterns = [ #api/
    # jwt
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    path('register/', views.UserDetailAPI.as_view()),
    path('get-details/', views.UserDetailAPI.as_view()),

    path('', include(router.urls)),
]