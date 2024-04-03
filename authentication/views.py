
# authentication/views.py
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from authentication.forms import EmailAuthenticationForm
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm  # Import your custom login form

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful signup
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def custom_login(request):
    error_message = None  # Initialize error_message to None initially
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print(f"Email: {email}, Password: {password}")  # Debugging statement
            print(str(request))
            user = auth.authenticate(request, username=email, password=password)
            print(f"Authentication result: {user}")  # Debugging statement
            if user is not None:
                print("User authenticated successfully.")  # Debugging statement
                login(request, user)
                messages.success(request, 'Login successful.')
                return redirect('home')  # Redirect to the home page after login
            else:
                print("Authentication failed.")  # Debugging statement
                error_message = 'Invalid email or password.'
        else:
            print("Form is not valid.")  # Debugging statement
            error_message = 'Form is not valid.'
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form, 'error_message': error_message})