from django.shortcuts import render, get_object_or_404
from django.views.generic import (View, TemplateView, ListView, DetailView,
                                    CreateView,UpdateView,DeleteView)
# from django.http import HttpResponse
from . import models

class BoardListView(ListView):
    context_object_name = 'boards'
    model = models.Board

class BoardDetailView(DetailView):
    context_object_name = 'board_detail'
    model = models.Board
    template_name = 'chan_app/board_detail.html'
    def get_context_data(self,**kwargs):
        data = super().get_context_data(**kwargs)
        threads = models.Thread.objects.all()
        threadCount = 0
        for thread in threads:
            if str(thread.board.id) == self.kwargs['pk']:
                threadCount= threadCount + 1
        data['thread_count'] = threadCount
        return data

class ThreadDetailView(DetailView):
    context_object_name = 'thread_detail'
    model = models.Thread
    template_name = 'chan_app/thread_detail.html'
    def get_context_data(self,**kwargs):
        data = super().get_context_data(**kwargs)
        posts = models.Post.objects.all()
        postCount = 0
        for post in posts:
            if str(post.thread.id) == self.kwargs['pk']:
                postCount= postCount + 1
        data['post_count'] = postCount
        return data

class ThreadCreateView(CreateView):
    fields = ('board','thread_name')
    model = models.Thread

class PostCreateView(CreateView):
    fields = ('thread','post_text','pic')
    #fields = ('thread_name',)##TODO
    model = models.Post
