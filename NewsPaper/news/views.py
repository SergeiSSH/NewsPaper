from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.core.paginator import Paginator
from django.views.generic import View, ListView, DetailView, DeleteView, UpdateView, CreateView, TemplateView
from .models import *
from datetime import datetime
from .filter import PostFilter
from .form import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class PostList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-id')
    paginate_by = 2

    form_class = PostForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.now(tz=None)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


#   def get_context_data(self, **kwargs):
#       context = super().get_context_data(**kwargs)
#       context['time_now'] = datetime.utcnow()
#       context['value1'] = None
#       return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
    queryset = Post.objects.all()


class AddPost(CreateView):
    model = Post
    template_name = 'addpost.html'
    form_class = PostForm
    success_url = '/news/'


class EditPost(UpdateView):
    model = Post
    template_name = 'addpost.html'
    form_class = PostForm

    def get_post(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

    success_url = '/news/'


class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    form_class = PostForm
    queryset = Post.objects.all()
    success_url = '/news/'


'''def author_list(request):
    au = author_filter(request.Get, queryset=Author.objects.all())
    return render(request, '.html', {'filter': au})


def date_list(request):
    d = data_filter(request.Get, queryset=Post.objects.all())
    return render(request, '.html', {'filter': d})

def filter_post(request):
    f=PostFilter(request.Get, queryset=Post.objects.all())
    return render(request, 'search.html', {'filter': f})
'''

class Subscribe(LoginRequiredMixin, View):
    def post(self, request, **kwargs):
        user = request.user
        category = get_object_or_404(Category, id=kwargs['pk'])
        if category.cat_sub.filter(username=request.user).exists():
            category.cat_sub.remove(user)
        else:
            category.cat_sub.add(user)

        return redirect(request.META['HTTP_REFERER'])
