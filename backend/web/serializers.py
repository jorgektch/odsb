from rest_framework import serializers, routers, viewsets
from .models import *

class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = ('name', 'logo')


class OdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ods
        fields = ('name', 'logo')


class InformationSourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformationSources
        fields = ('name', 'image', 'institutions', 'year', 'tipe', 'number_of_queries', 'description')
        