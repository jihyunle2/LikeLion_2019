from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog,Comment
from .forms import BlogPost
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    blogs = Blog.objects
    #
    blog_all=Blog.objects.all()
    paginator = Paginator(blog_all,3)
    page=request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'home.html', {'blogs':blogs,'posts':posts})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    #
    if request.method=="POST":
          Comment.objects.create(
                blog=details,
                comment_author=request.POST.get('comment_author'),
                comment_contents=request.POST.get('comment_contents')
          )
          return redirect('/blog/'+str(details.id))

    return render(request, 'detail.html',{'details':details})

def comment_delete(request,blog_id,comment_id):
      details = get_object_or_404(Blog, pk=blog_id)
      comment = get_object_or_404(Comment, pk=comment_id)
      comment.delete()
      return redirect('/blog/'+str(details.id))

def new(request):
      return render(request, 'new.html')

def create(request):
      blog = Blog()
      blog.title = request.POST['title']
      blog.pub_date = timezone.datetime.now()
      blog.body = request.POST['body']
      blog.save()
      return redirect('/blog/'+str(blog.id))

def delete(request, blog_id):
    destroy = get_object_or_404(Blog,pk=blog_id)
    destroy.delete()
    return redirect('home')


def update(request, blog_id):
    updates=get_object_or_404(Blog, pk=blog_id)
    return render(request, 'update.html',{'updates':updates})

def edit(request, blog_id):
    edit = Blog.objects.get(pk=blog_id)
    edit.title = request.POST['title']
    edit.pub_date = timezone.datetime.now()
    edit.body = request.POST['body']
    edit.save()
    return redirect('home')


def blogpost(request):
      if request.method == 'POST':
            form = BlogPost(request.POST)
            if form.is_valid():
                  post = form.save(commit=False)
                  post.pub_date=timezone.now()
                  post.save()
                  return redirect('home')
      else:
            form = BlogPost()
            return render(request, 'new.html', {'form':form})
