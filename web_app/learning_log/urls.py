"""learning_log URL Configuration

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
from learning_logs import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),

    # Home page.
    url(r'^$', views.index, name='index'),

    # Show all topics.
    url('topics', views.topics, name='topics'),

    # Detail page for a single topic.
    url(r'^topic/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    # Page for adding a new topic.
    url(r'^new_topic/$', views.new_topic, name='new_topic'),

    # Page for adding a new entry.
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

    # Page for editing an entry.
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),

    # Users
    url(r'^users/', include('users.urls', namespace='users'))
]
