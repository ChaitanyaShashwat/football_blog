from django.http import HttpResponse
from django.shortcuts import render
from articles.models import Article


def home(request):
    articles = Article.objects.all().order_by('-date')
    return render(request,'homepage.html',{'articles':articles})

def about(request):
    return render(request,'about.html')

def join(request):
    return render(request,'join_us.html')

def submit(request):
    return render(request,'render.html')
