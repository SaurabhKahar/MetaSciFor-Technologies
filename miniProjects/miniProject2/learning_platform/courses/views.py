from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from .models import Course
from django.contrib.auth.decorators import login_required
from .forms import SignupForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import LoginForm    
from django import forms


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main_page')  # Redirect to the main page after login
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()

    return render(request, 'courses/login.html', {'form': form})


class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data

def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()
            return redirect('login')  # Redirect to login after signup
    else:
        form = SignupForm()

    return render(request, 'courses/signup.html', {'form': form})

@login_required
def course_list(request):
    # Retrieve all available courses and pass them to the template
    courses = Course.objects.all()
    return render(request, 'courses/main_page.html', {'courses': courses})

def user_logout(request):
    logout(request)  # Logs out the user
    return redirect('login')  # Redirect to the login page after logging out

@login_required
def main_page(request):
    return render(request, 'courses/main_page.html')


def course_cpp(request):
    return render(request, 'courses/course_cpp.html')

def course_csharp(request):
    return render(request, 'courses/course_csharp.html')

def course_python(request):
    return render(request, 'courses/course_python.html')

def course_java(request):
    return render(request, 'courses/course_java.html')

def course_ruby(request):
    return render(request, 'courses/course_ruby.html')

def course_aws(request):
    return render(request, 'courses/course_aws.html')

def path_web_development(request):
    return render(request, 'courses/path_web_development.html')

def path_application_development(request):
    return render(request, 'courses/path_application_development.html')

def path_cyber_security(request):
    return render(request, 'courses/path_cyber_security.html')

def path_data_science(request):
    return render(request, 'courses/path_data_science.html')

def path_mobile_development(request):
    return render(request, 'courses/path_mobile_development.html')

def path_game_development(request):
    return render(request, 'courses/path_game_development.html')

@login_required
def user_profile_view(request):
    user = request.user  # Get the logged-in user
    # You can add more context here as needed
    context = {
        'user': user,
        # Add other data you want to display in the profile
    }
    return render(request, 'courses/user_profile.html', context) 
