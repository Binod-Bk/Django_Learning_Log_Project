from django.shortcuts import render
from .models import Topic

# Create your views here.

def index(request):
    """The home page for learning log."""
    return render(request, 'learning_logs/index.html')

def about_us(request):
    """The about us page for learning log."""
    return render(request, 'learning_logs/about_us.html')

def topics(request):
    """Show all Topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)