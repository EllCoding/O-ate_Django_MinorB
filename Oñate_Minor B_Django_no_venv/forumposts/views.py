from django.shortcuts import render
from rest_framework import generics, permissions
from .models import ForumPost, ForumComment
from .serializers import ForumPostSerializer, ForumCommentSerializer


class ForumPostListCreateView(generics.ListCreateAPIView):
    queryset = ForumPost.objects.all().order_by('-created_at')
    serializer_class = ForumPostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ForumPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ForumPost.objects.all().order_by('-created_at')
    serializer_class = ForumPostSerializer
    permission_classes = [permissions.IsAuthenticated]


class ForumCommentListCreateView(generics.ListCreateAPIView):
    queryset = ForumComment.objects.all().order_by('-commented_at')
    serializer_class = ForumCommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(commenter=self.request.user)


class ForumCommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ForumComment.objects.all().order_by('-commented_at')
    serializer_class = ForumCommentSerializer
    permission_classes = [permissions.IsAuthenticated]
