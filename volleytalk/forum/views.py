from django.shortcuts import render, HttpResponse
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def post(request):
    all_posts = Post.objects.all
    if request.method == 'POST':
        form = PostForm(request.POST or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            form.save()
        return render(request, 'forum.html', {'all_posts': all_posts})
    else:
        return render(request, 'forum.html', {'all_posts': all_posts})

def comment(request):
    all_comments = Comment.objects.all
    if request.method == 'POST':
        form = CommentForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, 'forum.html', {'all_comments': all_comments})

    else:
        return render(request, 'forum.html', {'all_comments': all_comments})









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
