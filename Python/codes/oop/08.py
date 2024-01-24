class Circle: # __str__ # 매직 메서드
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r # self.r * self.r 해야함. r * r이 아니다
    # 인스턴스를 프린트 할 때 결과로 나오는 값
    def __str__(self):
        return f'[원] radius: {self.r}' # {r} 이렇게 하면 값이 안나옴


c1 = Circle(10)
c2 = Circle(1)

print(c1.area()) # 314.0

print(c1)  # [원] radius: 10
print(c2)  # [원] radius: 1



# class Circle: # __str__ # 매직 메서드

#     def area(self,r):
#         return 3.14 * r * r 
#     # 인스턴스를 프린트 할 때 결과로 나오는 값
#     def __str__(self):
#         return f'[원] radius: {self.r}'
# c1 = Circle()
# print(c1.area(4))