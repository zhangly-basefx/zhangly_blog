from django.shortcuts import render
from django.shortcuts import redirect
from activate.models import Activate
from django.contrib.auth.models import User


def activate(request,code):
    activate = Activate.objects.get(activate_code=code)
    user = activate.user
    user.is_active = True
    user.save()
    return render(request,"activate.html",{"username":user.username})
