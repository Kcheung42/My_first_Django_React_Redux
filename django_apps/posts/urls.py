from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
		PostDetailAPIView,
		PostListAPIView,
		post_create,
		post_delete,
		post_detail,
		post_home,
		post_list,
		post_update,
)

urlpatterns = [
		url(r'^$', post_home),
		url(r'^(?P<id>\d+)/$', post_detail, name='detail'),
		url(r'^api/$', PostListAPIView.as_view(), name='list-api'),
		url(r'^api/(?P<id>\d+)/$', PostDetailAPIView.as_view(), name='detail-api'),
		url(r'^create/$', post_create),
		url(r'^delete/$', post_delete),
		url(r'^list/$', post_list, name='list'),
		url(r'^update/$', post_update),
]

#This
urlpatterns = format_suffix_patterns(urlpatterns)
