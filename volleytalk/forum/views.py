from django.shortcuts import render, HttpResponse
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def forum(request):
    all_posts = Post.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.likes.set(None)
            form.save()
        return render(request, 'forum.html', {'all_posts': all_posts})
    else:
        return render(request, 'forum.html', {'all_posts': all_posts})
    
def post(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            form.save()
        return render(request, 'post.html', {'post': post})
    else:
        return render(request, 'post.html', {'post': post})
            

# def comment(request):
#     form = CommentForm()
#     print(request.post)
#     if request.method == 'POST':
#         form = CommentForm(request.POST or None)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.author = request.user
#             comment.post = request.post
#             form.save()
#         return render(request, 'forum.html', {'form': form})

#     else:
#         return render(request, 'home.html')









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
