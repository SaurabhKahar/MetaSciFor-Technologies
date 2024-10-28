from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .form import SignupForm  

from django.contrib import messages  

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Set hashed password
            user.save()
            # Instead of redirecting, add a success message and render the same page
            messages.success(request, 'You have signed up successfully. Please log in.')
            form = SignupForm()  # Reset the form after successful signup
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('landing')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')


def profile(request):
    return render(request, 'profile.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('landing')

def landing(request):
    return render(request, 'landing.html')

def explore(request):
    return render(request, 'explore.html')

def packages(request):
    return render(request, 'packages.html')

@login_required
def bookings(request):
    return render(request, 'bookings.html')

def bookings_redirect(request):
    messages.warning(request, "Please log in to access the bookings page.")
    return redirect('login')  # Assuming your login URL name is 'login'

def contact(request):
    return render(request, 'contact.html')

def terms_conditions(request):
    return render(request, 'terms.html')

def faq(request):
    return render(request, 'faq.html')

def about(request):
    return render(request, 'about.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        user = request.user
        user.email = request.POST.get('email')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.save()
        messages.success(request, 'Your profile has been updated successfully.')
        return redirect('profile')  # Redirect to the profile page after saving

    return redirect('profile')  # Redirect if the method is not POST

