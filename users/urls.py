"""URL patterns for users"""

from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    #defualt auth URL
    path('', include('django.contrib.auth.urls')),
    path('', views.registration, name='register')
]
