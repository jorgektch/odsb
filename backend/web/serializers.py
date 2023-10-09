from rest_framework import serializers, routers, viewsets
from .models import *

class InstitutionSerializar(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = ('name', 'logo')


class OdsSerializar(serializers.ModelSerializer):
    class Meta:
        model = Ods
        fields = ('name', 'logo')


class InformationSourcesSerializar(serializers.ModelSerializer):
    class Meta:
        model = InformationSources
        fields = ('name', 'image', 'institutions', 'year', 'tipe', 'number_of_queries', 'description')
        