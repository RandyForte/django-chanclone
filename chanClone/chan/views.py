from django.shortcuts import render
from chan.forms import newPost, newThread
from chan.models import Post, Board, Thread
from django.views.generic import View,TemplateView,ListView,DetailView
# Create your views here.

# def index(request):
#     return render(request,'chan/index.html')
class IndexView(TemplateView):
    template_name = 'index.html'

class BoardListView(ListView):
    context_object_name = 'boards'
    model = Board

class ThreadListView(ListView):
    context_object_name = 'threads'
    model = Thread

class PostListView(ListView):
    context_object_name = 'posts'
    model = Post
