from django.urls import path, include
from .views import IndexView

urlpatterns = [
    path('accounts/login', include('allauth.urls')),
    path('', IndexView.as_view())
]