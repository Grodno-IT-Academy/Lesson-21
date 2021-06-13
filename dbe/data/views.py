from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

# Create your views here.
def home_page(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'data/home.html', context)

def article_page(request, article_id):
    article = Article.objects.get(id=article_id)
    article.count_views += 1
    article.save()
    context = {
        'article': article
    }
    return render(request, 'data/article.html', context)

from django.core.signals import request_started
from django.dispatch import receiver
from .models import Request


@receiver(request_started)
def finished_request(sender, environ, **kwargs):
    # print(sender,help(sender.get_response))
    path = environ['PATH_INFO']
    if Request.objects.filter(url=path):
        request = Request.objects.get(url=path)
        request.count += 1
        request.save()
    else:
        Request.objects.create(url=path, count=1)
    # print(environ['PATH_INFO'])
    # Request.object.create()
    # print("nada")