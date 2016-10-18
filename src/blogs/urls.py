from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^posts/$', PostList.as_view(), name="post_list"),
    url(r'^posts/(?P<pk>\d+)/$', PostDetail.as_view()),
]
