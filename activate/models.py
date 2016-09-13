from django.db import models
from django.contrib.auth.models import User

class Activate(models.Model):
    user = models.ForeignKey(User,verbose_name="用户名")
    activate_code = models.CharField("激活码",max_length=100)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "激活"
        verbose_name_plural= "激活"
