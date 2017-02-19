from django.db import models
from django.contrib.auth.models import User

class Information(models.Model):
    owner = models.ForeignKey(User,verbose_name="作者")
    content = models.CharField("消息内容",max_length=100)
    link = models.CharField("消息链接",max_length=100)
    status = models.IntegerField("状态",choices=((0,"已读"),(-1,"未读")))

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "消息"
        verbose_name_plural = "消息"
