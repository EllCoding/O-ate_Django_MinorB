from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import ForumPost, ForumComment

User = get_user_model()

class ForumCommentSerializer(serializers.ModelSerializer):
    commenter_username = serializers.CharField(source='commenter.username', read_only=True)

    class Meta:
        model = ForumComment
        fields = ['id', 'post', 'commenter', 'commenter_username', 'comment', 'commented_at']


class ForumPostSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)
    comments = ForumCommentSerializer(many=True, read_only=True)

    class Meta:
        model = ForumPost
        fields = ['id', 'author', 'author_username', 'content', 'created_at', 'comments']
