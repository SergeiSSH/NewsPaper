

from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view()),

    path('create/', AddPost.as_view(), name='addpost'),
    path('edit/<int:pk>', EditPost.as_view(), name='editpost'),

    #path('edit/<int:pk>', EditPost.as_view(), name='addpost'),
    path('delete/<int:pk>', DeletePost.as_view(), name='delete_post'),
    #path('search/', author_list),
    path('search/', filter_post),

    path('', include('signup.urls')),
    path('', include('protect.urls')),
    path('sign/', include('signup.urls')),
    path('accounts/', include('allauth.urls')),
    path('accounts/login', include('allauth.urls')),



    ]