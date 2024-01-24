class Person:
    def __init__(self):
        print('인스턴스가 생성되었습니다.')


person1 = Person()  # 인스턴스가 생성되었습니다.


class Person:
    def __init__(self, name):
        print(f'인스턴스가 생성되었습니다. {name}')
        # self.name = name 할당 안해서, print(person1.name) 에러나옴


person1 = Person('지민')  # 인스턴스가 생성되었습니다. 지민
print(person1.name)
