"""Define URL Patterns for Learning Logs."""

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    #Home Page
    path('',views.index, name='index'),
    path('',views.about_us, name='about_us'),
    path('topics/',views.topics, name='topics'),
]