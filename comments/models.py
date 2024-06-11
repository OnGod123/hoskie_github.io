from django.db import models
from django.contrib.auth.models import User
from .models import BlogPost, ImagePost, VideoPost  # Import all content models (optional)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey('contenttypes.ContentType', on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = models.GenericForeignKey('content_types.ContentType', 'object_id')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} commented on {self.content_object}"

    class Meta:
        ordering = ['created_at']  # Order comments by creation date

