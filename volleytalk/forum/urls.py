from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="homepage"),
    path("home", views.home, name="homepage"),
    path('polls', views.polls, name='polls'),
    path('rankings', views.rankings, name='rankings'),
    path('news', views.news, name='news'),
    path('players', views.players, name='players'),
    path('clubs', views.clubs, name='clubs'),
    path('forum', views.post, name='forum'),
    path('forum', views.comment, name='forum'),
]