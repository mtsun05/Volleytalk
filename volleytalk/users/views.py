from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from .forms import RegisterForm

# Create your views here.
class RegisterView(generic.CreateView):
  form_class = UserCreationForm
  template_name = 'registration/register.html'
  success_url = reverse_lazy('login')