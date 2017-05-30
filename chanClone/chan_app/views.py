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

class ThreadDetailView(DetailView):
    context_object_name = 'thread_detail'
    model = models.Thread
    template_name = 'chan_app/thread_detail.html'

class ThreadCreateView(CreateView):
    fields = ('board','thread_name')#TODO remove if works
    model = models.Thread

class PostCreateView(CreateView):
    fields = ('thread','post_text','pic')
    #fields = ('thread_name',)##TODO
    model = models.Post
