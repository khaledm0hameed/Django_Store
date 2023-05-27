from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RegistrationForm

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            User.objects.create_user(username=username, password=password, email=email)
            return redirect('register:login')
    else:
        form = RegistrationForm()
    
    return render(request, 'register/signup.html', {'form': form})


