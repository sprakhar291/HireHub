from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import *
# Create your views here.

def register(request):
    if request.method == 'POST':
        form=UserRegistrationForm((request.POST))
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=UserRegistrationForm()
    D={'form':form}
    return render(request, 'accounts/register.html', D)

def login_view(request):
    if request.method == 'POST':
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('dashboard')
    else:
        form=AuthenticationForm()
    D={'form':form}
    return render(request, 'accounts/login.html', D)

@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')