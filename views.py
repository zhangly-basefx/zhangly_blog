from django.shortcuts import render
from block.models import Block
from django.contrib.auth.models import User
from django.shortcuts import redirect
import uuid
from activate.models import Activate
def index(request):
    block_infos = Block.objects.filter(status=0).order_by("-id")
    return render(request,"index.html",{"blocks":block_infos})

def create_user(request,):
    if request.method == "GET":
        return render(request,"create_user.html")
    else:
        
        username = request.POST["username"]
        email    = request.POST["email"]
        password = request.POST["password"]
        rpassword = request.POST["rpassword"]
        errorStr = ("~","`","!","@","#","$","%","^","&","*","(",")","-","=","+","{","}","[","]",":",";","\"","'","\\")
        if not(username and email and password and rpassword):
            return render(request,"create_user.html",{"username":username,"email":email,"error":"注册内容不能为空."})
        if password != rpassword:
            return render(request,"create_user.html",{"username":username,"email":email,"error":"两次输入的密码不同."})
        if len(username) > 10:
            return render(request,"create_user.html",{"username":username,"email":email,"error":"用户名超出长度10."})
        if len(password) > 20:
            return render(request,"create_user.html",{"username":username,"email":email,"error":"密码超出长度20."})
        if User.objects.filter(username=username).exists():
            return render(request,"create_user.html",{"username":username,"email":email,"error":"用户名已经存在."})
        if User.objects.filter(email=email).exists():
            return render(request,"create_user.html",{"username":username,"email":email,"error":"此邮箱已注册."})



        user = User.objects.create_user(username,email,password)
        user.is_active = False
        user.save()
        user2 = User.objects.get(username=username)
        activate_code = str(uuid.uuid4())
        activate = Activate(user2,activate_code)
        activate.save()
        return redirect("/re_succeed")

def re_succeed(request):
    return render(request,"cUser_ok.html")
