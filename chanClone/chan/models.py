from django.db import models

# Create your models here.
class Board(models.Model):
    board_name = models.CharField(max_length=255)

class Thread(models.Model):
    board = models.ForeignKey(Board,on_delete=models.CASCADE,related_name='threads')
    thread_name = models.CharField(max_length=255)

class Post(models.Model):
    thread = models.ForeignKey(Thread,on_delete=models.CASCADE,related_name='posts')
    post_text = models.TextField(max_length=255)#text field
    pic = models.ImageField(blank=True,null=True,upload_to='post_img')
