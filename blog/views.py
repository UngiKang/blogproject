from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Blog
from django.utils import timezone

# Create your views here.
def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs' : blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog': blog_detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()    #사용하기 위해서는 위에 from django.utils import timezone 을 입력
    blog.writer = request.user
    blog.save()
    return redirect('/blog/'+str(blog.id))
    #여기서 str은 문자열 더하기를 위한 형변환임.