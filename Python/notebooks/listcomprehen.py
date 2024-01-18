# 똑같은 리스트를 만드는데 세 가지 방법

numbers = ['1','2','3']
# => [1, 2, 3] 으로 바꾼 새로운 리스트 생성

# 1 일반 for문 (권장)
new_numbers = [] # 새로운 리스트를 생성하기 위해 새 바구니를 만듦.
for number in numbers:
    new_numbers.append(int(number))
print(new_numbers)
    
# 2 map함수 (2차원 배열)
new_numbers2 = list(map(int, numbers))
print(new_numbers2)

# 3 list comprehension (for문이 주어졌을 때 작성은 할 수 있어야함)
# [표현식 for 변수 in 이터러블]
new_numbers3 = [int(number) for number in numbers] #for문을 먼저 써보고 작성해보기
print(new_numbers3)