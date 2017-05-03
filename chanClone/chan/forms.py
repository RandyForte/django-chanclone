from django import forms
from chan.models import Post, Thread

class newPost(forms.ModelForm):
    class Meta():
        model = Post
        fields = '__all__'

class newThread(forms.ModelForm):
    class Meta():
        model =  Thread
        fields = '__all__'
