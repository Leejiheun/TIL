class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email


class Student(Person):
    def __init__(self, name, age, number, email, student_id): # 설정해줘야함
        self.name = name
        self.age = age
        self.number = number
        self.email = email
        self.student_id = student_id

class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        super().__init__(name, age, number, email)
        Person().__init__(name, age, number, email)
        self.student_id = student_id
# 다중상속이 일어났을 때가 있기 때문에 Person을 써줌