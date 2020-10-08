"""blog URL ConfigurationrseMatch at /users/login/
'learning_logs' is not a registered namespace

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from blogApp import views

urlpatterns = [
    path('', views.index, name="index"),
    path(r'^post/(?P<blog_id>\d+)/$', views.post, name="blog_post"),
    path('blog_posts/', views.blog_posts, name="blog_posts"),
    path('new_blog_post/', views.new_blog_post, name="new_blog_post"),
    url(r'^edit_blog_post/(?P<blog_id>\d+)/$', views.edit_blog_post, name='edit_blog_post'),

    # Admin
    path('admin/', admin.site.urls),

    # Users
    path('users/', include('users.urls', namespace='users'))
]
