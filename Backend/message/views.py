from flask_sqlalchemy import Model
from rest_framework.viewsets import ModelViewSet
from . import models, serializers


class GenericFileUploadView(ModelViewSet):
    queryset = models.GenericFileUpload.objects.all()
    serializer_class = serializers.GenericFileUploadSerializer  