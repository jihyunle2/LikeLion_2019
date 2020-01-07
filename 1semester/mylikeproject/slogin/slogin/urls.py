
from django.contrib import admin
from django.urls import path, include
import login.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login.views.home,name='home'),
    path('accounts/',include('allauth.urls')),
]
