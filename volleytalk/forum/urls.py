from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path('polls', views.polls, name='polls'),
    path('rankings', views.rankings, name='rankings'),
    path('news', views.news, name='news'),
    path('players', views.players, name='players'),
    path('clubs', views.clubs, name='clubs'),
    path('forum', views.forum, name='forum'),
    path('post/<int:id>', views.post, name='post')
]