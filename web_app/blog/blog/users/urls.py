from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    # Login Page
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    url(r'^register/$', views.register, name='register')
]

app_name = 'users'