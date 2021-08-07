from django.conf import settings
from django.urls import include, path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
]
