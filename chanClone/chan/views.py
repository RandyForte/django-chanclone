from django.shortcuts import render
from chan.forms import newPost
from chan.models import Post
# Create your views here.

# def index(request):
#     return render(request,'chan/index.html')

def index(request):
    return render(request,'chan/index.html',context=myDict)

def thread(request):
    makePost = newPost()
    posts = Post.objects.all()
    myDic = {'post':posts,'makePost':makePost}
    if request.method == 'POST':
        form = newPost(request.POST,request.FILES)
        if form.is_valid():
            form.pic = form.cleaned_data['pic']
            form.save(commit=True)
            return index(request)
    return render(request,'chan/thread.html',context=myDic)
