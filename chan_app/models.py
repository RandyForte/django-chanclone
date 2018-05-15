from django.db import models
from django.urls import reverse
from PIL import Image
# Create your models here.
class Board(models.Model):
    board_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=3)

    def __str__(self):
        return self.board_name


class Thread(models.Model):
    board = models.ForeignKey(Board,on_delete=models.CASCADE,related_name='threads')
    thread_name = models.CharField(max_length=255)
    thread_text = models.CharField(max_length=255,null=True)
    thread_image = models.ImageField(blank=True,null=True,upload_to='thread_images')

    def __str__(self):
        return self.thread_name

    def get_absolute_url(self):
        return reverse("chan_app:threaddetail",kwargs={'pk':self.pk,'board_id':self.board_id})

class Post(models.Model):
    thread = models.ForeignKey(Thread,on_delete=models.CASCADE,related_name='posts')
    post_text = models.TextField(max_length=255)#text field
    post_image = models.ImageField(blank=True,null=True,upload_to='post_images')

    def get_absolute_url(self):
        return reverse("chan_app:threaddetail",kwargs={'pk':self.pk,'board_id':self.pk})
