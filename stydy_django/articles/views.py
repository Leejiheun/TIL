from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    # context 데이터는 렌더링하는 템플릿에서 사용하기위한 데이터
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    # 몇번 게시글인지 조회할 때 사용하는
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

def new(request):
    form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)

def create(request):
    #  요청 메서드가 POST 라면
    if request.method == 'POST':
        # 1. 데이터를 받고
        form = ArticleForm(request.POST)
        # 2. 유효성 검사
        # 2.1 검사 성공  => 데이터 저장하고 redirect
        if form.is_valid():
            article = form.save()
            return redirect('article:detail', article.pk)    
    # 요청 메서드가 POST가 아니라면
    else:
        form = ArticleForm()
    context = {
        'form':form,
    }
     # 2.2 검사 실패  => 에러메시지를 포함한 form을 출력하는 new 템플릿을 응답
    return render(request, 'articles/create.html', context)