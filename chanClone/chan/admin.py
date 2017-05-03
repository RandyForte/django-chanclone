from django.contrib import admin
from chan.models import Post, Board, Thread

# Register your models here.
admin.site.register(Board)
admin.site.register(Post)
admin.site.register(Thread)
