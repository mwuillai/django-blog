from django.shortcuts import render, redirect
from .models import Articles
from django.views import generic
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def index(request):
    articles = Articles.objects.order_by('-creation_date')[:5]
    for article in articles:
        article.article = "{}...".format(article.article[:100])
    return render(request, 'blog/index.html', {'articles': articles})


class Article(generic.DetailView):
    model = Articles
    template_name = 'blog/article.html'

""" 
def inscription(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.refresh_from_db()
            profile_form = ProfileForm(request.POST, instance=user.profile)
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            return render(request, "index.html")
    else:
        form = UserCreationForm()
    return render(request, 'blog/inscription.html', {'form': form}) """
