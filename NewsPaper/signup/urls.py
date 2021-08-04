from django.urls import path, include

urlpatterns = [
    path('', include('protect.urls')),
    path('sign/', include('sign.urls'))

]
