from django.contrib import admin
from chan_app.models import Board,Thread,Post
# Register your models here.

admin.site.register(Board)
admin.site.register(Thread)
admin.site.register(Post)
