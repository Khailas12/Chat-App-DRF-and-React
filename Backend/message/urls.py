from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import GenericFileUploadView


router = DefaultRouter(trailing_slash=False)
router.register('file-upload/', GenericFileUploadView)

urlpatterns = [
    path('', include(router.urls)),
]