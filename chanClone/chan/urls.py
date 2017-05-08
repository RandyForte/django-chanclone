from django.conf.urls import url
from chan import views

app_name = 'chan'

urlpatterns = [
    url(r'^$',views.BoardListView.as_view(),name='list'),
    #url(r'^s/',views.board,name='board'),
]
