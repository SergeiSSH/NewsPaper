from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.core.paginator import Paginator
from django.views.generic import View, ListView, DetailView, DeleteView, UpdateView, CreateView, TemplateView
from .models import *
import datetime
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
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.datetime.now(tz=None)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context

    form_class = PostForm

    @login_required()
    def new(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid:
            form.save()
        return super().get(request, *args, **kwargs)


class PostDetail(PermissionRequiredMixin, DetailView):
    permission_required = ('news.add_post', 'news.change_post')
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
    queryset = Post.objects.all()


    def comment_view(self, **kwargs):
        comments = Comment.objects.get(commentPost=self.kwargs['pk']).order_by('-id')
        return comments



class AuthorList(ListView):
    model = Author
    template_name = 'authorlist.html'
    context_object_name = 'authorlist'
    queryset = Author.objects.all().order_by('-ratingAuthor')


class AuthorView(DetailView):
    model = Author
    template_name = 'author.html'
    context_object_name = 'author'
    queryset = Author.objects.all()


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


class Comments(DetailView):
    model = Comment
    context_object_name = 'comments'


class CategoryList(ListView):
    model = Category
    template_name = 'categories.html'
    context_object_name = 'categories'
    queryset = Category.objects.all().order_by('name')


class CategoryView(ListView):
    model = PostCategory
    template_name = 'viewcategory.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['filter'] = Category.objects.filter(id=self.kwargs['pk'])
        return context

    def get_queryset(self):
        return Post.objects.filter(postCategory=self.kwargs['pk']).order_by('-dateCreation')


class Subscribe(LoginRequiredMixin, View):
    def post(self, request, **kwargs):
        user = request.user
        category = get_object_or_404(Category, id=kwargs['pk'])
        if category.subs.filter(username=request.user).exists():
            category.subs.remove(user)
        else:
            category.subs.add(user)

        return redirect(request.META['HTTP_REFERER'])
