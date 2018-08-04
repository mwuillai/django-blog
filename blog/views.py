from django.shortcuts import render
from .models import Articles
from django.views import generic

# Create your views here.


def index(request):
    articles = Articles.objects.order_by('-creation_date')[:5]
    for article in articles:
        article.article = "{}...".format(article.article[:100])
    return render(request, 'blog/index.html', {'articles': articles})


class Article(generic.DetailView):
    model = Articles
    template_name = 'blog/article.html'
