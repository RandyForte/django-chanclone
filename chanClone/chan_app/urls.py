from django.conf.urls import url
from chan_app import views

app_name = 'chan_app'

urlpatterns = [
    url(r'^/',views.IndexView.as_view(),name='index'),
    url(r'^boards$',views.BoardListView.as_view(),name='boardlist'),
    url(r'^(?P<pk>[-\w]+)/$',views.BoardDetailView.as_view(),name='boarddetail'),
    url(r'^(?P<board_id>[-\w]+)/(?P<pk>[-\w]+)/$',views.ThreadDetailView.as_view(),name='threaddetail'),
    url(r'^(?P<board_id>[-\w]+)/create',views.ThreadCreateView.as_view(),name='create'),
]
