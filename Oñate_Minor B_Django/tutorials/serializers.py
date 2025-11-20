from rest_framework import serializers
from .models import Tutorial, TutorialComment

class TutorialCommentSerializer(serializers.ModelSerializer):
    commenter_username = serializers.CharField(source='commenter.username', read_only=True)

    class Meta:
        model = TutorialComment
        fields = ['id', 'tutorial', 'commenter', 'commenter_username', 'comment', 'commented_at']


class TutorialSerializer(serializers.ModelSerializer):
    created_by_username = serializers.CharField(source='created_by.username', read_only=True)
    comments = TutorialCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Tutorial
        fields = ['id', 'title', 'content', 'created_by', 'created_by_username', 'created_at', 'comments']
