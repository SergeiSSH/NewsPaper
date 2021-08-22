from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('protect.urls')),
    path('sign/', include('signup.urls')),
    path('register/', include('signup.urls')),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('news/', include('news.urls')),
    path('', include('news.urls')),
    path('accounts/', include('allauth.urls')),

]
