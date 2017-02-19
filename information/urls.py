from django.conf.urls import url
from .views import showInfo
from .views import readInfo
from .views import setInfo
urlpatterns=[
        url(r'^list/',showInfo),
        url(r'^read/(?P<information_id>\d+)',readInfo),
        url(r'^setInfos/',setInfo)

        ]
