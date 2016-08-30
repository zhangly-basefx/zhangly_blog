from django.shortcuts import render
from block.models import Block
from article.models import Article
def article_list(request,block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    articles_objs=Article.objects.filter(block=block,status=0).order_by("-id")
    return render(request,"article_list.html",{"articles":articles_objs,"b":block})

def submit(request,block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)

    return render(request,"submit.html",{"b":block})
