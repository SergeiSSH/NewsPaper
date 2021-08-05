


from django.urls import path, include
from .views import PostList, PostDetail, AddPost, EditPost, PostFilter,filter_post, DeletePost


urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view()),

    path('create/', AddPost.as_view(), name='addpost'),
    path('edit/<int:pk>', EditPost.as_view(), name='editpost'),

    #path('edit/<int:pk>', EditPost.as_view(), name='addpost'),
    path('delete/<int:pk>', DeletePost.as_view(), name='delete_post'),
    #path('search/', author_list),
    path('search/', filter_post),







    ]