# views.py
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest, JsonResponse
from .models import Like, BlogPost, ImagePost, VideoPost

@login_required
def like_post(request, post_id):
    if request.method != 'POST':
        return HttpResponseBadRequest()

    try:
        post_id = int(post_id)
    except ValueError:
        return HttpResponseBadRequest()

    content_type = request.POST.get('content_type')
    if content_type not in ('blog_post', 'image_post', 'video_post'):
        return HttpResponseBadRequest()

    user = request.user

    if content_type == 'blog_post':
        post = get_object_or_404(BlogPost, pk=post_id)
    elif content_type == 'image_post':
        post = get_object_or_404(ImagePost, pk=post_id)
    else:
        post = get_object_or_404(VideoPost, pk=post_id)

    like, created = Like.objects.get_or_create(user=user, post_id=post_id, content_type=content_type)
    like.liked = not like.liked  # Toggle like status
    like.save()

    if like.liked:
        post.likes.add(user)
    else:
        post.likes.remove(user)

    post.like_count = post.likes.count()
    post.save()

    response_data = {'like_status': like.liked, 'total_likes': post.like_count}
    return JsonResponse(response_data)

