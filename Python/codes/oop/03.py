class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1


person1 = Person('iu')
person2 = Person('BTS')

print(Person.count)  # 2


class Circle:
    pi = 3.14

    def __init__(self, r):
        self.r = r

    def notice(self): 
        return f'이 원의 반지름은 {self.r}입니다' 

c1 = Circle(5)
c2 = Circle(10)

print(c1.notice())
print(c2.notice())