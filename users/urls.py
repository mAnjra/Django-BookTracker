"""URL patterns for users"""

from django.urls import path, include

app_name = 'users'
urlpatterns = [
    #defualt auth URL
    path('', include('django.contrib.auth.urls')),
]
