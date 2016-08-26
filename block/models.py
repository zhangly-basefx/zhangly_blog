from django.db import models


class Block(models.Model):
    name = models.CharField("版块名称",max_length=100)
    desc = models.CharField("版块描述",max_length=100)
    manager_name = models.CharField("版块管理员名称",max_length=100)

