class ParentA:
    def __init__(self):
        self.value_a = 'ParentA'

    def show_value(self):
        print(f'Value from ParentA: {self.value_a}')


class ParentB:
    def __init__(self):
        self.value_b = 'ParentB'

    def show_value(self):
        print(f'Value from ParentB: {self.value_b}')


class Child(ParentA, ParentB):
    def __init__(self):
        # self.value_a = 'ParentA' # 이게 생략되어져있다.
        super().__init__() # 여기서는 ParentA의 생성자 함수를 가져옴
        self.value_c = 'Child'

    def show_value(self):
        super().show_value()
        print(f'Value from Child: {self.value_C}') # ParentA 활용

child = Child()
child.show_value()
print(child.value_a)