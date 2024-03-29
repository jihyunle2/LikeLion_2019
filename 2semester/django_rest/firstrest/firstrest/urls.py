
from django.contrib import admin
from django.urls import path,include
import post.urls
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/',include('post.urls')),
    path('userpost/',include('userpost.urls')),
    path('api-auth/',include('rest_framework.urls')),
    path('api-token-auth/',obtain_auth_token),
]
