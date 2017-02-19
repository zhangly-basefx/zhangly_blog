from django.conf.urls import url

from .views import article_list
from .views import submit
from .views import article_detail
urlpatterns=[
    url(r'^list/(?P<block_id>\d+)',article_list),
    url(r'^create/(?P<block_id>\d+)',submit),
    url(r'^detail/(?P<article_id>\d+)',article_detail),

]
