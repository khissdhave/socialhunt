from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView
from django.utils.timezone import now
from bs4 import BeautifulSoup
import requests
from .models import SearchRecord
from .sites import SITES

# Registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in automatically after registration
            messages.success(request, 'Registration successful!')
            return redirect('search')  # Redirect to the homepage or any other view
        else:
            messages.error(request, 'Registration failed. Please check the form and try again.')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('search')  # Redirect to the homepage or any other view
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})



@login_required
def index(request):
    return render(request, 'search.html')

@login_required
def search_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        search_links = [site + username for site in SITES]
        # Save search record
        SearchRecord.objects.create(user=request.user, username=username, search_time=now())
        return render(request, 'search.html', {'search_links': search_links})
    return render(request, 'search.html')
