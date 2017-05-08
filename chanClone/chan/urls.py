from django.conf.urls import url
from chan import views

urlpatterns = [
    url(r'^index/',views.index,name='index'),
    url(r'^s/',views.board,name='board'),
]
