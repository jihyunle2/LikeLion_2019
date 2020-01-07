from django.shortcuts import render
from django.utils import timezone
from .models import Blog

from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class BlogView(ListView):
    #template_name='blogapp/list.html'
    model=Blog

class BlogCreate(CreateView):
    model=Blog
    #context_object_name='blogpost'
    fields=['title','body']
    success_url = reverse_lazy('list')

class BlogDetail(DetailView):
    model=Blog

class BlogUpdate(UpdateView):
    model=Blog
    fields=['title','body']
    success_url = reverse_lazy('list')

class BlogDelete(DeleteView):
    model=Blog
    success_url = reverse_lazy('list')



