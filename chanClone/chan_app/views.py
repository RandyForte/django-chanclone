from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (View, TemplateView, ListView, DetailView,
                                    CreateView,UpdateView,DeleteView)
# from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.http import HttpResponse
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
            if str(thread.board.slug) == self.kwargs['slug']:
                threadCount= threadCount + 1
        data['thread_count'] = threadCount
        return data

    def post(self, request, slug):
        b = models.Board.objects.get(slug=slug)
        print(str(request))
        newthread = models.Thread.objects.create(
        thread_name=request.POST.get("thread_name"),
        board=b,
        thread_text=request.POST.get("thread_text"))
        return redirect(reverse('chan_app:boarddetail', kwargs={'slug':slug}))

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

class PostCreateView(CreateView):
    fields = ('thread','post_text','pic')
    #fields = ('thread_name',)##TODO
    model = models.Post
