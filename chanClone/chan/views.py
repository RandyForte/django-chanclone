from django.shortcuts import render
from chan.forms import newPost, newThread
from chan.models import Post, Board, Thread
from django.views.generic import View,TemplateView,ListView,DetailView
# Create your views here.

# def index(request):
#     return render(request,'chan/index.html')
