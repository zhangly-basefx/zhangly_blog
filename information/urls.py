from django.conf.urls import url
from .views import showInfo
from .views import readInfo

urlpatterns=[
        url(r'^list/',showInfo),
        url(r'^read/(?P<information_id>\d+)',readInfo),

        ]
