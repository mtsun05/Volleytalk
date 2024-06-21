from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path('polls', views.polls, name='polls'),
    path('rankings', views.rankings, name='rankings'),
    path('news', views.news, name='news'),
    path('players', views.players, name='players'),
    path('clubs', views.clubs, name='clubs'),
    path('forum', views.post, name='forum'),
    path('forum', views.comment, name='forum'),
]