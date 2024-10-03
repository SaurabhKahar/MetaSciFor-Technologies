"""
URL configuration for learning_platform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from courses import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.user_login, name='home'),  # Default to the login page
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('main/', views.main_page, name='main_page'),  # Main page after login

    path('course/cpp/', views.course_cpp, name='course_cpp'),
    path('course/csharp/', views.course_csharp, name='course_csharp'),
    path('course/python/', views.course_python, name='course_python'),
    path('course/java/', views.course_java, name='course_java'),
    path('course/ruby/', views.course_ruby, name='course_ruby'),
    path('course/aws/', views.course_aws, name='course_aws'),
    path('path/web-development/', views.path_web_development, name='path_web_development'),
    path('path/application-development/', views.path_application_development, name='path_application_development'),
    path('path/cyber-security/', views.path_cyber_security, name='path_cyber_security'),
    path('path/data-science/', views.path_data_science, name='path_data_science'),
    path('path/mobile-development/', views.path_mobile_development, name='path_mobile_development'),
    path('path/game-development/', views.path_game_development, name='path_game_development'),
    path('profile/', views.user_profile_view, name='user_profile'),  # Add this line
]
