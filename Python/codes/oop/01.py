class Person:
    # 속성/변수
    blood_color = 'red' # 클래스 변수

    def __init__(self, name): # 생성자 함수, 초기값 # 객체 생성할 때 호출
        self.name = name # 인스턴스 변수

    def singing(self):
        return f'{self.name}가 노래합니다.'


# 인스턴스 생성
singer1 = Person('iu')
# 생성을 했으니깐 메서드(두개) 호출 / 인스턴스가 사용할 수 있는 메서드는 두번째꺼 뿐
print(singer1.singing())  # iu가 노래합니다.


# 속성(변수) 접근
print(singer1.blood_color)  # red
