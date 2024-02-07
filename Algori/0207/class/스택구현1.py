def push(n):
    global top
    top += 1
    if top == size:
        print('Overflow!')
    else:
        stack[top] = n

top = -1
size = 10
stack = [0] * 10

top += 1
stack[top] = 10

top += 1
stack[top] = 20

push(30)

while top >= 0:
    top -= 1
    print(stack[top+1])

# 스택을 이용해서 문제 푸는 과정 이해
# top size를 이용해서 구현할 수 있다