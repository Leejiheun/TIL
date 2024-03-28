from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    # 모델 폼의 정보를 입력하는 곳
    # 왜 class이고 이름이 Meta인지는 그냥 Django 개발자들이 이렇게 구성해둔거임
    # model과 fields 변수는 필수 작성이다.
    class Meta:
        model = Article
        fields = '__all__'