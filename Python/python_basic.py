def get_sum(num1, num2):
    return num1+num2
num1 =5
num2 =3
result = get_sum(num1, num2)
print(result)

def get_sum2(num1, num2):
    return num1 + num2
result = get_sum2(5,3)
print(result)

def greet(name):
    return 'Hello'+ name
result = greet('ALICE')
print(result)

def greet(name, age):
    print(f'안녕하세요 {name}님 {age}살 이에요')
greet('Sally', 26)