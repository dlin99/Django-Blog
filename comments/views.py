from django.shortcuts import render, get_object_or_404
from .models import Comment
from .forms import CommentForm

from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def comment_delete(request, pk):
    # obj = get_object_or_404(Comment, id=pk)
    try:
        obj = Comment.objects.get(id=pk)
    except:
        raise Http404

    if obj.author != request.user:
        # messages.success(request, "You do not have permission to view this.")
        # raise Http404
        response = HttpResponse("You do not have permission to do this.")
        response.status_code = 403
        return response

    if request.method == "POST":
        parent_obj_url = obj.content_object.get_absolute_url() # the parent post
        obj.delete()
        messages.success(request, "This comment has been deleted.")
        return HttpResponseRedirect(parent_obj_url)

    context = {
        'object': obj
    }
    return render(request, 'comments/confirm_delete.html', context)




def comment_thread(request, pk):
    # obj = get_object_or_404(Comment, id=pk)  # grab the comment
    try:
        obj = Comment.objects.get(id=pk)
    except:
        raise Http404

    if not obj.is_parent:
        obj = obj.parent

    content_object = obj.content_object # the Post that related the this comment
    content_id = obj.content_object.id

    initial_data = {
            "content_type": obj.content_type,
            "object_id": obj.object_id
    }

    form = CommentForm(request.POST or None, initial=initial_data)

    if form.is_valid() and request.user.is_authenticated:
        content_type = ContentType.objects.get_for_model(obj.content_object.__class__)
        obj_id = form.cleaned_data.get('object_id')
        content_data = form.cleaned_data.get("content")
        parent_obj = None
        try:
            parent_id = int(request.POST.get("parent_id")) # from the form
        except:
            parent_id = None

        if parent_id:
            parent_qs = Comment.objects.filter(id=parent_id)
            if parent_qs.exists() and parent_qs.count() == 1:
                parent_obj = parent_qs.first()


        new_comment, created = Comment.objects.get_or_create(
                            author = request.user,
                            content_type= content_type,
                            object_id = obj_id,
                            content = content_data,
                            parent = parent_obj,
                        )
        return HttpResponseRedirect(new_comment.content_object.get_absolute_url()) # go back to the POST


    context = {
        "comment": obj,
        "form": form,
    }
    return render(request, 'comments/comment_thread.html', context)
