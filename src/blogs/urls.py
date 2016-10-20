from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$', BlogList.as_view(), name="blog_list"),
    url(r'^(?P<pk>\d+)/posts/$', PostList.as_view(), name="post_list"),
    url(r'^(?P<blog>\d+)/posts/(?P<pk>\d+)/$', PostDetail.as_view(), name="post_detail"),
]
