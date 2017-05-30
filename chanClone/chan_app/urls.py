from django.conf.urls import url
from chan_app import views

app_name = 'chan_app'

urlpatterns = [
    # url(r'^$',views.IndexView.as_view(),name='index'),#code for the old index page
    url(r'^$',views.BoardListView.as_view(),name='index'),
    url(r'^(?P<pk>[-\w]+)/$',views.BoardDetailView.as_view(),name='boarddetail'),
    url(r'^(?P<board_id>[-\w]+)/(?P<pk>[-\w]+)/$',views.ThreadDetailView.as_view(),name='threaddetail'),
    url(r'^(?P<board_id>[-\w]+)/createthread',views.ThreadCreateView.as_view(),name='createthread'),
    url(r'^(?P<board_id>[-\w]+)/(?P<pk>[-\w]+)/newpost',views.PostCreateView.as_view(),name='createpost'),
]
