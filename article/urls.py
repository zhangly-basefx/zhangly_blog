from django.conf.urls import url

from .views import article_list
from .views import submit
urlpatterns=[
    url(r'^list/(?P<block_id>\d+)',article_list),
    url(r'^create/(?P<block_id>\d+)',submit)


]
