from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .models import *
from .serializers import *

class InstitutionViewSet(viewsets.ModelViewSet):
    queryset = Institution.objects.all().order_by('-date_joined')
    permission_classes = [permissions.AllowAny]
    serializer_class = InstitutionSerializar

class OdsViewSet(viewsets.ModelViewSet):
    queryset =  Ods.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = OdsSerializar

class InformationSourcesViewSet(viewsets.ModelViewSet):
    queryset = Institution.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = InformationSourcesSerializar

# Create your views here.
