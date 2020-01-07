from django.shortcuts import render, redirect, get_object_or_404 #render: 페이지를 생성해주겠다

# Create your views here.
from .models import Posting
from django.utils import timezone

def home(request):
    posts=Posting.objects
    context ={"posts":posts}
    return render(request,'home.html',context)

def new(request):
    return render(request,'new.html')

def create(request):
    post = Posting()
    post.title = request.POST['title']
    post.body=request.POST['body']
    post.pub_date=timezone.datetime.now()
    post.image=request.FILES['image']
    post.save()
    return redirect("home")

#read
def detail(request, post_id):
    post=get_object_or_404(Posting, pk=post_id)
    context = {"post":post}
    return render(request, 'detail.html',context)



