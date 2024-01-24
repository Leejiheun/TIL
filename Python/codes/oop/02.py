# Person 정의
class Person:
    name = 'unknown' # 클래스 변수

    def talk(self): #  talk 라는 인스턴스 메서드
        print(self.name)


p1 = Person()
p1.talk()  # unknown

# p2 인스턴스 변수 설정 전/후
p2 = Person()
p2.talk()  # unknown

p2.name = 'Kim' # p2의 인스턴스 변수 'Kim'
p2.talk()  # talk메서드 호출하면 # Kim # p2는 kim이라는 인스턴스변수 가지게 됨
print(Person.name)  # unknown # class 도 직접작으러 접근 가능
print(p1.name)  # unknown # 인스턴스들도 class접근가능
print(p2.name)  # Kim #p2는 name이라는 변수가 본인한테 인스턴스 변수가 있기 때문에 kim이 출력

p2.ssafy = 11
print(p2.ssafy) # 독립적이기때문에, # 어떤 인스턴스 변수여도 상관없음