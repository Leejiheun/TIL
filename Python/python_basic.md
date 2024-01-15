# 파이썬
## 타입
- Numeric Type
  - int(정수), float(실수), complex(복소수)
- Text Sequence Type
  - str(문자열)

## 산술연산자
---
- : 음수부호
+ : 덧셈, - : 뺄셈
* : 곱셈
/ : 나눗셈, // : 몫, % : 나머지, ** : 지수(거듭제곱)
---
- 연산자 우선순위
: ** > -(음수부호) > * / // % > + -(뺄셈)

## 변수를 할당하다
- 영문, _ , 숫자로 구성
- 숫자로 시작할 수 없음
- 대소문자 구문

```
number = 10
double = 2 * number
print(double) # 20

number = 5
print(double) # 20
```

# Str 문자열 표현
```
print('Hello World)
print(type('Hello World))

```
\n : 줄바꿈
\t : 탭
\\ : 백슬래시
\' : 작은 따옴표
\" : 큰 따옴표
ex)
```
print('이 다음은 엔터\n 입니다')
이 다음은 엔터
입니다
``

## f-str
```
counts = 13
area = 'living room'
print(f'Debugging {area} {counts}')
-> Debugging living room 13
```

##  시퀀스 특징
my_str = 'hello'
print(my_str[1]) # e
print(my_str[2:4]) # ll
print(my_str[0:5:2]) #hlo
print(my_str[::-1]) #olleh
```
password = "In the bustling city, where life is a constant race against time, uoy often find yourself wondering if there's a shortcut to success. The vibrant lights of the cityscape illuminate the night, casting shadows on the short-lived dreams of those who seek fortune. As you navigate through the crowded streets, you realize the deen for guidance, like a compass pointing python. You need direction in this chaotic journey called life."
# 아래에 코드를 작성하시오.
first_char = password[28:36]
second_word = password[113:118]
third_word = password[68:65:-1] #you
fourth_word = password[322:326][::-1]
fifth_word = password[365:371]
print(first_char)
print(second_word)
print(third_word)
print(fourth_word)
print(fifth_word)
```