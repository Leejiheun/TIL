# 4개의 클래스, 최상위는 Person이고 Person을 상속받는게 Mom과 Dad, 
# FirstChild는 Mom과 Dad로부터 다중상속 받음
class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f'안녕, {self.name}'


class Mom(Person):
    gene = 'XX'

    def swim(self):
        return '엄마가 수영'


class Dad(Person):
    gene = 'XY'

    def walk(self):
        return '아빠가 걷기'


class FirstChild(Dad, Mom): # 이러면 다중상속 # Dad가 먼저 상속받음
    # XX, XY -> 중복된 메서드(gene)가 있다면 다중상소일 때 먼저 상속받은게 나옴
    def swim(self):
        return '첫째가 수영'
    
    def cry(self):
        return '첫째가 응애'
baby1 = FirstChild('김싸피') # 생성자 함수가 없으면 상속받는거 위로 찾아서 올라가기. Person에 생성자함수가 있음
print(baby1.cry())
print(baby1.swim())
print(baby1.walk())
print(baby1.gene)