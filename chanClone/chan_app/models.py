from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
class Board(models.Model):
    board_name = models.CharField(max_length=255)

    def __str__(self):
        return self.board_name


class Thread(models.Model):
    board = models.ForeignKey(Board,on_delete=models.CASCADE,related_name='threads')
    thread_name = models.CharField(max_length=255)

    def __str__(self):
        return self.thread_name

    def get_absolute_url(self):
        return reverse("chan_app:threaddetail",kwargs={'pk':self.pk,'board_id':self.board_id})

class Post(models.Model):
    thread = models.ForeignKey(Thread,on_delete=models.CASCADE,related_name='posts')
    post_text = models.TextField(max_length=255)#text field
    pic = models.ImageField(blank=True,null=True,upload_to='post_img')

    def get_absolute_url(self):
        return reverse("chan_app:threaddetail",kwargs={'pk':self.thread.id,'board_id':self.pk})
