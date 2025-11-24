from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Pet
from .serializers import PetSerializer


class PetListCreateView(generics.ListCreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class PetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()