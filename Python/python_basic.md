# 파이썬
## 타입
- Numeric Type
  - int(정수), float(실수), complex(복소수)
- Text Sequence Type
  - str(문자열)

## 산술연산자
```
- : 음수부호
+ : 덧셈, - : 뺄셈
* : 곱셈
/ : 나눗셈, // : 몫, % : 나머지, ** : 지수(거듭제곱)
```

- 연산자 우선순위
  ** > -(음수부호) > * / // % > + -(뺄셈)

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
print('Hello World')
print(type('Hello World'))
```

```
\n : 줄바꿈
\t : 탭
\\ : 백슬래시
\' : 작은 따옴표
\" : 큰 따옴표
```
```
print('이 다음은 엔터\n 입니다')
이 다음은 엔터
입니다
```

## f-str
```
counts = 13
area = 'living room'
print(f'Debugging {area} {counts}')
-> Debugging living room 13
```

##  시퀀스 특징
```
my_str = 'hello'
print(my_str[1]) # e
print(my_str[2:4]) # ll
print(my_str[0:5:2]) #hlo
print(my_str[::-1]) #olleh
```

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
## 1월 16일 화요일
### 시퀀스타입 특징
#### list [ ]
-> list 는 가변(변경 가능, str는 변경 불가능)
```
my_list = [1,2,3]
my_list[0] = 100
my_list = [100,2,3]
```

#### tuple ( )
-> 여러개의 값 순서대로 저장하되, 변경 불가능
my_tuple = (1,)

```
my_tuple = (1,'a',3,'b',5)
my_tuple[1] = 'z'
-> err
```
x, y = (10, 20) # 여러 개 값 할당 가능
- 파이썬은 쉼표를 튜플 생성자로 사용하니 괄호로 생략 가능
x, y = 10, 20 -> 개발자가 직접 사용하진 않는다.

- range

- 시퀀스 타입
- str, list, tuple, range

#### dic { }
- key-value쌍 - 순서 - 중복이없음 - 변경 가능함
- key는 불변만 사용 가능 (str)
- 두번째 요소인 list -> 틀린 문장!! bec) 순서가 없기 때문에
- 키를 통해 값에 접근, 값은 변경 가능 
- 순서가 없으면 인덱스가 존재하지 않는다, 키가 중복이 안되기 때문에 똑같은 값을 넣으면 마지막값이 출력됨

- set 순서와 중복이 없는 변경 가능한 자료형

- False : 0, True :1


## 1월 17일
### 함수
- 재사용성, 유지보수
```python
# 두수의 합을 구하는 함수
def get_sum(num1, num2):
    return num1 + num2
# 함수 사용하여 결과 출력
num1 = 5
num2 = 3
sum_result = get_sum(num1, num2)
print(sum_result)

-> Input (num1, num2) 부분
   Output sum_result
```
- 파라미터, 매개변수 : num1, num2 부분
- 반환 값 : return value

### 내장함수(built-in funtion)
- 기본적으로 제공하는 함수
```
- abs 절대값
result = abs(-1)
print(result) # 1
```
### 함수 정의와 호출
```python
# 함수 정의
def greet(name) :
  """입력된 이름 값에 인사하는 메세지를 만드는 함수"""
  message = 'Hello, ' + name
  return message
# 호출
result = greet('Alice')
print(result)
```
### 매개변수와 인자
- 매개변수(parameter) : 함수를 정의할 때, 함수가 받을 값을 나타내는 변수
- 인자(argument) : 함수를 호출할 때, 실제로 전달받는 값
#### 인자의 종류
- 위치 인자 : 
    ```python
    def greet(name, age):
      print(f'안녕하세요, {name}님! {age}살이시군요.')

    greet('Alice', 25) # 안녕하세요, Alice님! 25살이시군요.
    greet('Bella') # 타입에러 : 위치인자 없다. age라는 인자!
    greet(30, 'Bella') # 안녕하세요, 30님! Bella살이시군요.
    ```
- 기본 인자 :
  - 함수 정의에서 매개변수에 기본 값을 할당하는 것
  - 함수 호출 시 인자를 전달하지 않으면, 기본값이 매개변수에 할당됨
    ```python
    def greet(name, age=30):
        print(f'안녕하세요, {name}님! {age}살이시군요.')


    greet('Bob') # 안녕하세요, Bob님! 30살이시군요.
    greet('Charlie', 40) # 안녕하세요, Charlie님! 40살이시군요.
    ```
- 키워드인자
  - 함수 호출 시 인자의 이름과 함께 값을 전달하는 인자
  - 단, 호출 시 키원드 인자는 위치 인자 뒤에 위치해야 함

    ```python
    def greet(name, age):
        print(f'안녕하세요, {name}님! {age}살이시군요.')


    greet(name='Dave', age=35)  # 안녕하세요, Dave님! 35살이시군요.
    greet(age=35, 'Dave')  #  positional argument follows keyword argument # 'Dave'가 어디 위치인자인지 모름. 실행 안됨.
    ```
- 임의의 인자
  - 정해지지 않은 개수의 인자를 처리하는 인자
  - 함수 정의 시 매개변수 앞에 '*'를 붙여 사용하며, 여러 개의 인자를 tuple로 처리
    ```python
    def calculate_sum(*args):
        print(args)
        total = sum(args)
        print(f'합계: {total}')


    """
    (1, 2, 3)
    합계: 6
    """
    calculate_sum(1, 2, 3)
    ```
- 임의의 키워드 인자
  - 함수 정의 시 매개변수 앞에 '**'를 붙여 사용하며, dictionary로 묶어 처리
    ```python
    def print_info(**kwargs):
        print(kwargs)


    print_info(name='Eve', age=30) # {'name': 'Eve', 'age': 30}
    ```
### Python의 범위(Scope)

```
a = print(1)
print(a) # None
- 파이썬에서는 return이 없는 함수는 자동으로 None을 리턴
```