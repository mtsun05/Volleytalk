from django.shortcuts import render, HttpResponse
from .models import Ranking, Post
from .forms import PostForm

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def forum(request):
    all_posts = Post.objects.all
    if request.method == 'POST':
        form = PostForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, 'forum.html', {'all_posts': all_posts})

    else:
        return render(request, 'forum.html', {'all_posts': all_posts})










def rankings(request):
    items = Ranking.objects.all()
    return render(request, 'rankings.html', {'rankings': items})

def polls(request):
    items = Ranking.objects.all()
    return render(request, 'polls.html', {'polls': items})

def news(request):
    items = Ranking.objects.all()
    return render(request, 'news.html', {'news': items})

def clubs(request):
    items = Ranking.objects.all()
    return render(request, 'clubs.html', {'clubs': items})

def players(request):
    items = Ranking.objects.all()
    return render(request, 'players.html', {'players': items})
