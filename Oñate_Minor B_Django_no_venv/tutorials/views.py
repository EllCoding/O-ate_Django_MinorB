from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Tutorial, TutorialComment
from .serializers import TutorialSerializer, TutorialCommentSerializer


class TutorialListCreateView(generics.ListCreateAPIView):
    queryset = Tutorial.objects.all().order_by('-created_at')
    serializer_class = TutorialSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class TutorialDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tutorial.objects.all().order_by('-created_at')
    serializer_class = TutorialSerializer
    permission_classes = [permissions.IsAuthenticated]


class TutorialCommentListCreateView(generics.ListCreateAPIView):
    queryset = TutorialComment.objects.all().order_by('-commented_at')
    serializer_class = TutorialCommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(commenter=self.request.user)


class TutorialCommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TutorialComment.objects.all().order_by('-commented_at')
    serializer_class = TutorialCommentSerializer
    permission_classes = [permissions.IsAuthenticated]
