from django.conf.urls import url
from chan_app import views

app_name = 'chan_app'

urlpatterns = [
    url(r'^$',views.BoardListView.as_view(),name='list'),
    url(r'^(?P<pk>[-\w]+)/$',views.BoardDetailView.as_view(),name='detail'),
    url(r'^(?P<board_id>[-\w]+)/(?P<pk>[-\w]+)/$',views.ThreadDetailView.as_view(),name='detail'),
    url(r'^(?P<board_id>[-\w]+)/create',views.ThreadCreateView.as_view(),name='create'),
]
