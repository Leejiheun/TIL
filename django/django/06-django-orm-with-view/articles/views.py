from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all() # 전체데이터조회
    context = {
        'articles':articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk) # 특정한 번호 조회 / 단일데이터조회
    context = {
        'article':article,
    }
    return render(request, 'articles/detail.html', context)


def new(request):
    return render(request, 'articles/new.html')


def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    # print(request.GET) # <QueryDict: {'title': ['제목'], 'content': ['내용']}>
    
    # 1.
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2. 유효성 검사 넣어주고 앞으로 이 방식으로 사용할 것임
    article = Article(title=title, content=content)
    article.save()

    # 3. 유효성 검사 할 수 없음
    # Article.objects.create(title=title, content=content)

    # return render(request, 'articles/create.html')
    return redirect('articles:detail', article.pk)


def delete(request, pk):
    # 몇 번 글 삭제 할 거야? -> 조회를 먼저 해야 함
    article = Article.objects.get(pk=pk)
    article.delete() # 삭제 메서드
    return redirect('articles:index') # 삭제가 잘 되면 메인페이지로 요청감.


def edit(request, pk):
    article = Article.objects.get(pk =pk)
    context = {
        'article':article,
    }
    return render(request, 'articles/edit.html', context)


def update(request, pk):
    # 몇 번 게시글 수정? -> 조회
    article = Article.objects.get(pk=pk) # 먼저, 조회부터
 
    title = request.POST.get('title')
    content = request.POST.get('content')

    article.title = title
    article.content = content
    article.save()

    return redirect('articles:detail', article.pk)