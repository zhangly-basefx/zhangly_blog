from django.shortcuts import render
from django.shortcuts import redirect
from block.models import Block
from article.models import Article
from article.forms import ArticleForm
from django.core.paginator import Paginator

def article_list(request,block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    #articles_objs=Article.objects.filter(block=block,status=0).order_by("-id")
    ARTICLE_CNT_1PAGE = 3
    page_no = int(request.GET.get("page_no","1"))
    all_articles = Article.objects.filter(block=block,status=0).order_by("-id")
    p = Paginator(all_articles,ARTICLE_CNT_1PAGE)
    page = p.page(page_no)
    page_links = [i for i in range(page_no - 5,page_no+6) if i >0 and i <= p.num_pages]
    articles_objs = page.object_list
   
    return render(request,"article_list.html",{"articles":articles_objs,"b":block,"page":page,"plinks":page_links,"page_no":page_no})

def submit(request,block_id):
   block_id = int(block_id)
   block = Block.objects.get(id=block_id)
   if request.method == "GET":
       return render(request,"submit.html",{"b":block})
   else:
       form = ArticleForm(request.POST)
       if form.is_valid():
           article = form.save(commit=False)
           article.block  = block
           article.status = 0
           article.save()
           return redirect("/article/list/%s"%block_id)
       else:
           return render(request,"submit.html",{"b":block,"form":form})


def article_detail(request,article_id):
    article_id = int(article_id)
    article = Article.objects.get(id=article_id)
    block = Block.objects.get(name=article.block)
    return render(request,"article_detail.html",{"a":article,"b":block})
