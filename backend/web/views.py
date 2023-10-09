from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .models import *
from .serializers import *

class InstitutionViewSet(viewsets.ModelViewSet):
    queryset = Institution.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = InstitutionSerializer

class OdsViewSet(viewsets.ModelViewSet):
    queryset =  Ods.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = OdsSerializer

class InformationSourcesViewSet(viewsets.ModelViewSet):
    queryset = InformationSources.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = InformationSourcesSerializer

# Create your views here.
