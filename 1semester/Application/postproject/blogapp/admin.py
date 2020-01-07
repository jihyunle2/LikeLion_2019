from django.contrib import admin

# Register your models here.
#같은 파일 내에 있는 models   -> .models

from .models import Blog

admin.site.register(Blog)

