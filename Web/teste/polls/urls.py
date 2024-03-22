from django.urls import path
from . import views

urlPattern = [ 
    path("", views.index, name="index"),
]