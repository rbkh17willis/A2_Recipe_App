from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Recipe
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def home(request):
  return redirect('login')

class RecipeListView(ListView):
    model = Recipe
    template_name = "recipes/recipe_list.html"

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipes/recipe_details.html"

def login_view(request):
  error_message = None
  form = AuthenticationForm()

  if request.method == 'POST':
    form = AuthenticationForm(data = request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(username = username, password = password)
      if user is not None:
        login(request, user)
        return redirect('recipes:list')
    else:
      error_message = 'oops... something went wrong'
  context = {
    'form': form,
    'error_message': error_message
  }

  return render(request, 'auth/home.html', context)

def logout_view(request):
  logout(request)
  return render(request, 'auth/success.html')

