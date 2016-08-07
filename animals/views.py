from django.shortcuts import render

from animals.models import Animal
from rest_framework import viewsets
from animals.serializers import AnimalSerializer


class AnimalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer