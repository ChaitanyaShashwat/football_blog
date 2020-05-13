from django.shortcuts import render,redirect
from articles.models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def articles_home(request):
    articles = Article.objects.all().order_by('-date')
    return render(request,'articles/articles_home.html',{'articles':articles})

def news(request):
    articles = Article.objects.all().order_by('-date')
    return render(request,'articles/news.html',{'articles':articles})

def transfers(request):
    articles = Article.objects.all().order_by('-date')
    return render(request,'articles/transfers.html',{'articles':articles})

def analysis(request):
    articles = Article.objects.all().order_by('-date')
    return render(request,'articles/analysis.html',{'articles':articles})

def article_detail(request,slug):
    articleslug = Article.objects.get(slug=slug)
    return render(request,'articles/article_detail.html',{'article':articleslug})

@login_required(login_url = '/accounts/login')
def create(request):
    if request.method == "POST":
        form = forms.CreateArticle(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()

            return redirect("home_page")
    else:
        form = forms.CreateArticle
        return render(request,'articles/article_create.html',{'form':form})
