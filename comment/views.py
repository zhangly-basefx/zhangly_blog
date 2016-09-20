from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from comment.models import Comment
from article.models import Article
import json

def json_response(obj):
    txt = json.dumps(obj)
    return HttpResponse(txt)

def ifstatus(request):
    article_id = request.POST["article_id"]
    article_id = json.loads(article_id)
    content = request.POST["content"]
    owner = request.user
    article = Article.objects.get(id=article_id)
    if not content:
        return json_response({"status":"no","msg":"输入内容为空"})
    else:
        comment = Comment(owner=owner,article=article,content=content,status=0)
        comment.save()
        return json_response({"status":"ok","msg":"评论成功"})

