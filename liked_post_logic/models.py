# models.py
from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    likes = models.ManyToManyField(User, related_name='liked_blog_posts', blank=True)
    like_count = models.PositiveIntegerField(default=0)

class ImagePost(models.Model):
    image = models.ImageField(upload_to='images/')
    caption = models.TextField()
    likes = models.ManyToManyField(User, related_name='liked_image_posts', blank=True)
    like_count = models.PositiveIntegerField(default=0)

class VideoPost(models.Model):
    video = models.FileField(upload_to='videos/')
    description = models.TextField()
    likes = models.ManyToManyField(User, related_name='liked_video_posts', blank=True)
    like_count = models.PositiveIntegerField(default=0)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.PositiveIntegerField()
    content_type = models.CharField(max_length=50, choices=[
        ('blog_post', 'Blog Post'),
        ('image_post', 'Image Post'),
        ('video_post', 'Video Post'),
    ])
    liked = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} liked {self.get_content_type_display()}"

    class Meta:
        unique_together = (('user', 'post_id', 'content_type'),)

