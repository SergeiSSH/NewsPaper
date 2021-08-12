from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.core.paginator import Paginator
from django.views.generic import View, ListView, DetailView, DeleteView, UpdateView, CreateView, TemplateView
from .models import *
from datetime import datetime
from .filter import PostFilter
from .form import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Group
from django.core.mail import send_mail, EmailMultiAlternatives


class PostList(ListView, LoginRequiredMixin):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-id')
    paginate_by = 2

    form_class = PostForm

    '''def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.now(tz=None)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context'''

    @login_required()
    def new(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid:
            form.save()
        return super().get(request, *args, **kwargs)


#   def get_context_data(self, **kwargs):
#       context = super().get_context_data(**kwargs)
#       context['time_now'] = datetime.utcnow()
#       context['value1'] = None
#       return context


class PostDetail(PermissionRequiredMixin, DetailView):
    permission_required = ('news.add_post', 'news.change_post')
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
    queryset = Post.objects.all()


class AddPost(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post', 'news.change_post')
    model = Post

    template_name = 'addpost.html'
    form_class = PostForm
    success_url = '/news/'


class EditPost(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.add_post', 'news.change_post')
    User = "Authors"
    model = Post
    template_name = 'addpost.html'
    form_class = PostForm

    def get_post(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

    success_url = '/news/'


class DeletePost(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.add_post', 'news.change_post')
    model = Post
    template_name = 'delete_post.html'
    form_class = PostForm
    queryset = Post.objects.all()
    success_url = '/news/'


def filter_post(request):
    f = PostFilter(request.GET, queryset=Post.objects.all())
    return render(request, 'search.html', {'filter': f})


class Subscribe(LoginRequiredMixin, View):
    def post(self, request, **kwargs):
        user = request.user
        category = get_object_or_404(Category, id=kwargs['pk'])
        if category.subs.filter(username=request.user).exists():
            category.subs.remove(user)
        else:
            category.subs.add(user)

        return redirect(request.META['HTTP_REFERER'])
