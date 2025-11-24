from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class ForumPost(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='forum_posts'
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {self.author.username} on {self.created_at.strftime('%Y-%m-%d')}"

class ForumComment(models.Model):
    post = models.ForeignKey(
        ForumPost,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    commenter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='forum_comments'
    )
    comment = models.TextField()
    commented_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.commenter.username} on {self.commented_at.strftime('%Y-%m-%d')}"
   