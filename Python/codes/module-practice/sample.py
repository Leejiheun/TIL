from my_package.math import my_math
from my_package.statistics import tools
import requests # pip install requests

print(my_math.add(1, 2))
print(tools.mod(1, 2))


# my_package접근, math하고 my_math 임포트
# 모듈로 직접 접근 안됨. 패키지 거쳐서!