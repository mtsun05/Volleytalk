from django.shortcuts import render, HttpResponse
from .models import Post
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
    return render(request, 'rankings.html')

def polls(request):
    return render(request, 'polls.html')

def news(request):
    return render(request, 'news.html')

def clubs(request):
    return render(request, 'clubs.html')

def players(request):
    return render(request, 'players.html')
