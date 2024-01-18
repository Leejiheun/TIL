import my_math # 만들었던 my_math파일을 import

print(my_math.add(1, 2)) # 사용자가 정한 모듈을 활용






















'''
# 1과 2는 똑같음, 일반적으로 명시적인 코드는 #1이다. 
#2는 앞에 참조가 없기 때문에 pi가 개발자가 만들어낸 변수인지 모듈에서 가져온 건지 비교가 명확하지 않음.

# 1
import math

print(math.pi)
print(math.sqrt(4)) # 제곱근

# 2
from math import pi, sqrt

print(pi)
print(sqrt(4))
# print(help(math)) '''