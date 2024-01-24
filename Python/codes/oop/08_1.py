class Circle: # __str__ # 매직 메서드

    def area(self,r):
        return 3.14 * r * r 
    # 인스턴스를 프린트 할 때 결과로 나오는 값
    def __str__(self):
        return f'[원] radius: {self.r}'
c1 = Circle()
print(c1.area(4))