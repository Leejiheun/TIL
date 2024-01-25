class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self): # talk라는 메서드
        print(f'반갑습니다. {self.name}입니다.')


class Professor(Person): # 교수는 Person 클래스로부터 상속을 받는다
    def __init__(self, name, age, department): # 이름 나이 담당과목
        self.name = name
        self.age = age
        self.department = department

    def talk(self):
        print(f'잘 부탁드립니다.')
        
class Student(Person):
    def __init__(self, name, age, gpa): # 이름 나이 성적
        self.name = name
        self.age = age
        self.gpa = gpa


p1 = Professor('박교수', 59, '컴퓨터공학과')
s1 = Student('김학생', 20, 3.5)

print(p1.department) # 컴퓨터공학과
print(s1.gpa) # 3.5

p1.talk() # 반갑습니다. 박교수입니다.
s1.talk() # 반갑습니다. 김학생입니다.

# 각각의 교수 학생이 Person의 특징을 그대로 갖고 본인들이 필요한것을 갖는다
# 상속 받으면 됨. Person 에 괄호 X, Professor(Person) 이런식
