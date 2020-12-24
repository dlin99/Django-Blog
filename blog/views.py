from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    FormView,
)

from django.views.generic.detail import SingleObjectMixin
from .models import Post
from django.contrib.auth.models import User

from comments.forms import CommentForm
from comments.models import Comment
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse,  HttpResponseRedirect, HttpResponseForbidden

def home(request):
    # return HttpResponse('<h1>Blog Home</h1>')
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

# for the detail page, we need GET and POST functionality for the user to post new comment to the post
from django.views import View
class PostDetailView(View):

    def get(self, request, *args, **kwargs):
        view = PostDetailGetView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = PostDetailPostView.as_view()
        return view(request, *args, **kwargs)


class PostDetailGetView(DetailView):
    model = Post
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # content_type = ContentType.objects.get_for_model(Post)
        # obj_id = self.get_object().id
        # comments = Comment.objects.filter_by_instance(content_type=content_type, object_id=obj_id)
        instance = self.get_object()
        comments = instance.comments
        context['comments'] = comments

        initial_data = {
            'content_type': instance.get_content_type,
            'object_id': instance.id
            }
        comment_form = CommentForm(self.request.POST or None, initial=initial_data)
        context['comment_form'] = comment_form

        return context


class  PostDetailPostView(SingleObjectMixin, FormView):
    template_name = 'blog/post_detail.html'
    form_class = CommentForm
    model = Post

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        instance = self.get_object()
        initial_data = {
            'content_type': instance.get_content_type,
            'object_id': instance.id
            }
        comment_form = CommentForm(self.request.POST or None, initial=initial_data)

        if comment_form.is_valid():
            # c_type = comment_form.cleaned_data.get('content_type').split('|')
            content_type = ContentType.objects.get_for_model(instance.__class__)
            obj_id = comment_form.cleaned_data.get('object_id')
            content_data = comment_form.cleaned_data.get('content')
            parent_obj = None
            try:
                parent_id = int(self.request.POST.get("parent_id"))
            except:
                parent_id = None
            if parent_id:
                parent_qs = Comment.objects.filter(id=parent_id)
                if parent_qs.exists() and parent_qs.count() == 1:
                    parent_obj = parent_qs.first()

            new_comment, created = Comment.objects.get_or_create(
                                    author=request.user,
                                    content_type=content_type,
                                    object_id=obj_id,
                                    content=content_data,
                                    parent = parent_obj,
                                    )
            if created:
                print('it works!')

            return HttpResponseRedirect(self.get_success_url())
        else:
            print('fail!!!!!!!!!!!!!!!!!!!!!!!')
            return render_to_response(self.get_context_data(form=comment_form))


    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.get_object().id})


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    # return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about.html', {'title': 'About'})
