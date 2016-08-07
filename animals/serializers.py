from animals.models import Animal
from rest_framework import serializers


class AnimalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Animal
        fields = ('user_id', 'specie_id', 'name','physical_description', 'created_at', 'updated_at')

