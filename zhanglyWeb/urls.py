"""zhanglyWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin

import views
import activate.views
import comment.views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^article/',include('article.urls')),
    url(r'^$',views.index),
    url(r'^register',views.create_user),
    url(r'^re_succeed',views.re_succeed),
    url(r'^activate/(?P<code>[\w-]+)$',activate.views.activate),
    url(r'^accounts/',include('django.contrib.auth.urls')),
    url(r'^comment/create/',comment.views.ifstatus),
    url(r'^message/',include('information.urls')),
    url(r'^ueditor/',include('DjangoUeditor.urls')),

]

