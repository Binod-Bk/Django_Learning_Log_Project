"""Define URL Patterns for Learning Logs."""

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home Page
    path('',views.index, name='index'),
    path('',views.about_us, name='about_us'),
    path('topics/',views.topics, name='topics'),
    # Detail page for a single topic. (id)
    path('topics/<int:topic_id>/',views.topic, name='topic'),
    # Page for adding a new Topic using a form.
    path('new_topic/', views.new_topic, name='new_topic'),
]