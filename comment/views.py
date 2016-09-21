from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from comment.models import Comment
from article.models import Article
import json
from information.models import Information

def json_response(obj):
    txt = json.dumps(obj)
    return HttpResponse(txt)

def ifstatus(request):
    article_id = request.POST["article_id"]
    article_id = json.loads(article_id)
    info_link = request.POST["info_link"]
    content = request.POST["content"]
    page_number = request.POST["page_number"]
    pahe_number = json.loads(page_number)

    owner = request.user
    article = Article.objects.get(id=article_id)
    to_comment_id = int(request.POST.get("to_comment_id",0))
    if to_comment_id !=0:
        to_comment = Comment.objects.get(id=to_comment_id)
        info_content = "有人回复了你的评论'%s'"%(to_comment)
        info_link = info_link+"?page_no=%s"%(page_number)
    else:
        to_comment = None
        info_content = "有人回复了你的文章'%s'"%(article.title)
        info_link = info_link
    if not content:
        return json_response({"status":"no","msg":"输入内容为空"})
    else:
        information = Information(owner=article.owner,content=info_content,link=info_link,status=-1)
        information.save()
        comment = Comment(owner=owner,article=article,content=content,to_comment=to_comment,status=0)
        comment.save()
        return json_response({"status":"ok","msg":"评论成功"})

