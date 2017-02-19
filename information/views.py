from django.shortcuts import render
from django.shortcuts import redirect
from information.models import Information


def showInfo(request):
    msg_infos = Information.objects.filter(status=-1,owner=request.user)
    return render(request,"showInfo.html",{"msg":msg_infos})


def readInfo(request,information_id):
    msg_id = int(information_id)
    msg_info = Information.objects.get(id=msg_id)
    msg_info.status = 0
    msg_info.save()
    return redirect(msg_info.link)

def setInfo(request):
    msg_infos = Information.objects.filter(status=-1,owner=request.user)
    for i in msg_infos:
        i.status = 0
        i.save()
    return redirect("/message/list/")
