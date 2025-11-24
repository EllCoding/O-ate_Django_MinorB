from rest_framework import serializers
from .models import Pet

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = [
            'id',
            'name',
            'pet_type',
            'other_pet_type',
            'breed',
            'gender',
            'birth_date',
            'health',
            'favorite_food',
            'favorite_toy',
            'description',
            'status',
            'likes',
            'hates',
        ]
