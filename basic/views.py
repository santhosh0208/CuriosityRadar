from django.shortcuts import render
from .models import article

# Create your views here.

def home(request):
    article_list = article.objects.order_by('-published')
    return render(request, 'basic/home.html', {'articles': article_list})

def detail(request, url_title):
    display_article = article.objects.get(title = url_title)
    return render(request, 'basic/content.html', {'article': display_article})

