from django.db import models

# Create your models here.
# OOP 7, 8일차

# 상속 받는 부모 클래스 이름이 Model(대문자가 class)
# 모델스라는 모듈에 모델클래스를 상속받는 것.
# 열을 '필드'라고 함

# models.Model은 class 에서 상속 개념. 상속받는 
# 모델스라는 모듈에 모델을 상속받는 거
class Article(models.Model):
    # 설계도 작성(기본틀)
    title = models.CharField(max_length=10) # 모델스에서 가져온 클래스
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    uodated_at = models.DateTimeField(auto_now=True)
    
# 최종 테이블 이름은 "앱이름_모델클래스이름"으로 합성해서 만듦