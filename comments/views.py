from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseBadRequest
from .models import Comment, BlogPost, ImagePost, VideoPost  # Import all models (optional)

@login_required
def create_comment(request, content_type, object_id):
    if request.method != 'POST':
        return HttpResponseBadRequest()

    try:
        content_type_model = get_object_or_404(ContentType, model=content_type)
        model = content_type_model.model_class()
        content_object = get_object_or_404(model, pk=object_id)
    except (ValueError, LookupError):
        return HttpResponseBadRequest()

    user = request.user
    comment_text = request.POST.get('comment_text')

    if not comment_text:
        return HttpResponseBadRequest()

    comment = Comment.objects.create(user=user, content_type=content_type_model, object_id=object_id, text=comment_text)

    # Optional: Update comment count on the content object (implement logic as needed)
    # ...

    response_data = {'comment_id': comment.id, 'comment_text': comment.text, 'username': user.username}
    return JsonResponse(response_data)

