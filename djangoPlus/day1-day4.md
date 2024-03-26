# one_to_four (day1 ~ day4 까지 내용 복습 겸 정리)

자료: https://drive.google.com/drive/folders/1Zw-i2lgOufJ-MPSKur7g3645PYrJXdQD
구분: Django

- 바탕화면에서 one_to_four 파일 생성 후 vscode 로 열기

- 가상환경 만들기 > activate 하기 > django 설치 후  > 프로젝트 만들기 > 앱 2개 만들기
    
    ```jsx
    $ python -m venv venv_one_to_four  
    
    $ source venv_one_to_four/Scripts/activate
    
    $ pip install django
    
    $ django-admin startproject todo_list_pjt
    
    $ cd todo_list_pjt
    
    $ python manage.py runserver
    
    $ python manage.py startapp accounts
    
    $ python manage.py startapp todos
    ```
    

```jsx
# settings.py

---

INSTALLED_APPS = [
    'accounts',
    'todos',

---
```

```jsx
# todo_list_pjt > urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todos/', include('todos.urls')),
    path('accounts/', include('accounts.urls')),
]
```

accounts > [urls.py](http://urls.py) 파일 생성 

```jsx
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name='login')
]
```

accounts > views.py

```jsx
from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'accounts/login.html')

```

accounts 앱에서 templates>accounts>login.html 파일 생성 후

```jsx
<h1>로그인 페이지</h1>
<form action="#" method="GET">
  <label for="ssafy"></label>
  <input type="text" placeholder="유저네임" /> <br />
  <input type="password" placeholder="비밀번호" id="ssafy" name="query" /> <br />
  <input type="submit" value="login" />
</form>
```

- 서버 켜서 중간 확인
    - [urls.py](http://urls.py) 가서 todos/ 는 주석 처리를 하고 runserver 를 하자.
    - [http://127.0.0.1:8000/accounts/login/](http://127.0.0.1:8000/accounts/login/)  화면 확인 후

- 이제 todos 앱 셋팅 하자.
    - todos/ 주석 처리 한 것을 풀자.

todos > [urls.py](http://urls.py) 파일 생성

```jsx
from django.urls import path
from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.index, name='index'),
    path('create_todo/', views.create_todo, name='create_todo'),
    path('<work>/', views.detail, name='detail'),
]
```

index - 할일 리스트를 한눈에 보는 페이지

create_todo - 할일 목록을 생성하는 페이지

detail - 특정 할일의 세부 내용을 확인하는 페이지

todos > [views.py](http://views.py)

```jsx
from django.shortcuts import render

# Create your views here.

def index(request):
    pass

def create_todo(request):
    pass

def detail(request):
    pass
```

모든 html 문서에서 상속을 받는다.

base.html 문서를 만들고 상속을 하자.

해당 프로젝트 파일에 templates > base.html 만들자

templates > base.html

```jsx
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Don't think, Just do it</title>
  </head>
  <body>
    <a href="{% url 'todos:index' %}">[Main]</a>
    <a href="{% url 'todos:create_todo' %}">[Create]</a>
    <a href="{% url 'accounts:login' %}">[Login]</a>

    {% block content %}

    {% endblock %}
  </body>
</html>

```

그 다음 

[settings.py](http://settings.py) 파일의 'DIRS': [] 에다가

전역으로 적용시킬 템플릿이 들어가 있는 파일 경로를 적어주기

```jsx
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
        'APP_DIRS': True,
```

아까 만든 accounts 앱에서 상속받자

accounts > login.html

```jsx
{% extends 'base.html' %}

{% block content %}
  <h1>로그인 페이지</h1>
  <form action="#" method="GET">
    <label for="ssafy"></label>
    <input type="text" placeholder="유저네임" /> <br />
    <input type="password" placeholder="비밀번호" id="ssafy" name="query" /> <br />
    <input type="submit" value="login" />
  </form>
{% endblock %}
```

- 서버 켜서 확인해 보자. [http://127.0.0.1:8000/accounts/login/](http://127.0.0.1:8000/accounts/login/)

다시 todos 앱으로 돌아가서 먼저 할일 목록을 생성하는 create_todo 함수부터 작성

todos > [views.py](http://views.py)

```jsx
from django.shortcuts import render

# Create your views here.

def index(request):
    pass

def create_todo(request):
    return render(request, 'todos/create_todo.html')

def detail(request):
    pass
```

todos > templates > todos > create_todo.html 파일 생성

```jsx
{% extends 'base.html' %}

{% block content %}
  <h1>이곳에 할 일을 생성합니다.</h1>
  
  <form action="{% url 'todos:index' %}">
    <label for="create_todo"></label>
    <input type="text" id="create_todo" name="joy" />
    <input type="submit" value="go" />
  </form>
{% endblock %}
```

할일 생성한 것을 todos의 index 함수에서 받고 보여주자

todos > [views.py](http://views.py)

```jsx
from django.shortcuts import render

# Create your views here.

def index(request):
    work = request.GET.get('joy')
    context = {
        'work': work
    }
    return render(request, 'todos/index.html', context)
```

create_todo 의 form 을 통해서 입력받은 값을 

딕셔너리의 형태로 index 함수로 보냈고

index 함수에서는 context로 담아 index.html로 전달!!

todos > templates > todos > index.html 파일 생성

```jsx
{% extends 'base.html' %}

{% block content %}
  <h1>할 일 목록 상세 페이지</h1>

  <ul>
    {% if work %}
      <li>{{ work }}</li>
    {% else %}
      <li>아직 등록 된 할 일이 없습니다.</li>
    {% endif %}
  </ul>
{% endblock %}

```

index.html 에서는 전달 받은 값을 화면에 표기했다.

- 서버 켜서 확인해 보자. [http://127.0.0.1:8000/todos/create_todo/](http://127.0.0.1:8000/todos/create_todo/)

클릭 시 해당 work (할일)의 상세 페이지로 넘어가게 수정하자.

상세 페이지로 넘어가게 아래와 같이 링크를 달자.

```jsx
    {% if work %}
      <li>
        <a href="{% url 'todos:detail' work %}">{{ work }}</a>
      </li>
      
      
	      또는 아래와 같이 링크를 작성도 가능! 하지만 전자를 추천
        <a href="/todos/{{work}}">{{ work }}</a>
```

urls.py에서 상세페이지의 URL PATH 를 확인해 보니 variable routing 사용하고 있다.

따라서 'todos:detail' 옆에 work를 적어 줌으로써 

해당 URL에 함께 보낼 변수도 (variable) 작성해 주었다.

상세페이지 만들자.  

detail 함수에서는 URL에 들어갈 variable을 

매개변수 work 를 통해서 받자.

todos > views.py

```jsx
def detail(request, work):
    context = {
        'work': work
    }
    return render(request, 'todos/detail.html', context)
```

그리고 work값을 context를 통해서 detail.html 으로 전달했다.

templates > todos > detail.html 파일 생성

```jsx
{% extends "base.html" %}

{% block content %}
  <h1>{{ work }} 의 상세 페이지 입니다.</h1>
{% endblock content %}
```

- 서버켜서 creat 부터 detail 페이지 까지 잘 작동 되는지 확인해 보자

자, 그러면 이제 create에서 입력받은 할일을 database에 저장을 할 것이다.

models.py에 database의 테이블을 정의하자

todos > models.py

```jsx
from django.db import models

# Create your models here.

class Todo(models.Model):
    work = models.CharField(max_length=100)
    content = models.TextField()
    is_completed = models.BooleanField()
```

클래스를 정의 할 때 대문자로 작성하며 

models 모듈의 Model 클래스를 상속받아 DB 테이블을 작성했다.

```jsx
$ python manage.py makemigrations
$ python manage.py migrate
```

admin 계정도 생성하자

todos > admin.py

```jsx
from django.contrib import admin
from .models import Todo
# Register your models here.

admin.site.register(Todo)
```

```jsx
$ python manage.py createsuperuser
```

- 서버켜서 admin 페이지에서 로그인 까지 해서 확인해 보자.

===============================================

QuerySet API를 사용해서 데이터 베이스를 검색 정렬 그룹화 하는 것을 연습한다.

원래 database에서 데이터를 읽고 쓰고 조작할 때에는 SQL (Structured Query Language)

이라는 언어를 사용해서 데이터를 읽고 쓰는 등의 조작을 한다.

하지만 우리가 하려고 하는 것은 SQL문이 아닌, Django에서 파이썬을 사용해서 

DB에있는 데이터를 조작하려고 한다.

이때 파이썬과 같은 객체지향 언어로  DB에 있는 데이터를 조작할 수 있도록 

도와주는 컴퓨팅 기술을 ORM (Object-Relational-Mapping) 이라고 한다. 

그림으로 보자면 아래와 같다.

Django      ←—ORM—→  Database

(python)                             (data)

그리고 ORM 이  database에 있는  data를 읽고 쓰고 등의 조작을 할 때는 

QuerySet API 라는 도구를 사용해서 database로 요청을 보낸다.

본격적인 실습에 앞서, 실습 환경부터 조성하자.

===================================================

Django ORM 을 통해서 database에 데이터 CRUD 를 해 볼 것이다.

```jsx
$ pip install ipython
$ pip install django-extensions
$ pip freeze > requirements.txt
```

# ipython : 파이썬에서 사용하는 대화형 인터프리터 패키지

# django-extensions: 장고 편의기능들이 들어있는 패키지로, shell_plus 사용하기 위해 설치

```jsx
# settings.py
INSTALLED_APPS = [
	'accounts',
	'todos',
  'django_extensions',   # 언더바 주의
...,
]
```

```jsx
$ python manage.py shell_plus    # Django shell 실행하기
```

자 이제 django shell 에서 python 코드를 써서 database를 조작할 것이다. 

(이 과정을 도와주는 것이 ORM 이라고 했다.)

data를 조작하기 위해 database에 특정 데이터를 보내 달라는 요청하는 것을

“쿼리문을 작성한다!” 라고 하며, database로 쿼리문을 날리면 

ORM이 database에서 찾은 data를 QuerySet 이라는 자료형으로 

우리에게 data를 반환한다.

1. 자 그럼 query문으로 database에 data 객체를 생성 (Create) 볼 것이다. 그 다음
2. 데이터 들을 조회 (Read) 할 것이다.  - all filter get 등을 사용
3. 데이터를 수정 (Update)를 할 것이며, 
4. 데이터를 삭제 (Delete)도 할 것이다.

```jsx
In [1]: test=Todo(work='할일정보',content='상세정보',is_completed='False')

# 모든 데이터 조회
test.save()
test=Todo.objects.all()    
test[0].work

# 단일 데이터 조회
test=Todo.objects.get(pk=1)  
test.work

# 레코드 추가
test2=Todo.objects.create(work='두번째할일',content='노래연습',is_completed='False')

# 필드값 수정
test.work='첫번쨰할일'
test.save()

# 데이터 삭제
test.delete()

```

- db.sqlite3 로 확인 해보고
- 서버 켜서 admin 페이지에서도 확인 하자.

이번에는 레코드 작성 시간도 database에 기록이 되도록 테이블을 수정해보자.

todos > models.py

```jsx
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)
```

auto_now_add=True ( 최초 생성일자 )

auto_now=True (수정일자)

기존 Model에 새로운 필드를 추가하는 경우, 기존 Model 속 데이터들도 일괄적으로 변경되느데

새로운 필드에 값을 넣지 않을 경우, 에러가 발생하므로 Model에 새로운 필드를 추가 할 때는

default값을 설정해준다.

```jsx
$ python manage.py makemigrations
1 그리고 엔터 누른다.
$ python manage.py migrate
```

끝

[todo_list_pjt.zip](one_to_four%20(day1%20~%20day4%20%E1%84%81%E1%85%A1%E1%84%8C%E1%85%B5%20%E1%84%82%E1%85%A2%E1%84%8B%E1%85%AD%E1%86%BC%20%E1%84%87%E1%85%A9%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%20%E1%84%80%E1%85%A7%E1%86%B7%20%E1%84%8C%E1%85%A5%E1%86%BC%20c5c03705691d470b885fa652dfa1878c/todo_list_pjt.zip)