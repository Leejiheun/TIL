from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def new(request):
    return render(request, 'articles/new.html')


def create(request):
    # 1. 사용자가 입력한 데이터를 받아
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 2. 받은 데이터를 활용해서 게시글 작성
    article = Article(title=title, content=content) 
    article.save()

    # 3. redirect로 index
    return redirect('articles:index')
    