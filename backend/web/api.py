from .models import *
from rest_framework import viewsets, permissions
from .serializers import *

class InstitutionViewSet(viewsets.ModelViewSet):
    queryset = Institution.objects.all
    permission_classes = [permissions.AllowAny]
    serializer_class = InstitutionSerializar

class OdsViewSet(viewsets.ModelViewSet):
    queryset =  Ods.objects.all
    permission_classes = [permissions.AllowAny]
    serializer_class = OdsSerializar

class InformationSourcesViewSet(viewsets.ModelViewSet):
    queryset = InformationSources.objects.all
    permission_classes = [permissions.AllowAny]
    serializer_class = InformationSourcesSerializar