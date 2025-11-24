from django.db import models
from django.contrib.auth.models import User

class Tutorial(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tutorials'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class TutorialComment(models.Model):
    tutorial = models.ForeignKey(
        Tutorial,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    commenter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tutorial_comments'
    )
    comment = models.TextField()
    commented_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.commenter.username} on {self.tutorial.title}"