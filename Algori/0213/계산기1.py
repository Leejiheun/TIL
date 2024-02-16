T = 10
for tc in range(1, T+1):
    N = int(input())
    fx = input()
    st = []
    postfix = ''
    top = -1
    for tk in fx:
        if tk == '+':
            while st:
                if st[top] =='+' or st[top] == '*':
                    top += 1
                    postfix += st.pop()
                st.append(tk)
        elif tk == '*':
            while st:
                if st[top] =='+':
                    top += 1
                    postfix += st.pop()
                st.append(tk)
        else:
            postfix += tk
    while st:
        postfix += st.pop()

    for tk in postfix:
        if tk == '+':
            t1 = st.pop()
            t2 = st.pop()
            t3 = int(t1) + int(t2)
            st.append(t3)
        else:
            st.append(tk)
    print(f'#{tc} {st[0]}')

for x in range(10):
    n = int(input())
    st = []
    postfix = ''
    fx = input()

    for tk in fx:
        if tk == '+':
            while st:
                postfix += st.pop()
            st.append(tk)
        else:
            postfix += tk
    while st:
        postfix += st.pop()

    for tk in postfix:
        if tk == '+':
            t1 = st.pop()
            t2 = st.pop()
            t3 = int(t1) + int(t2)
            st.append(t3)
        else:
            st.append(tk)
    print(f'#{x+1} {st[0]}')

# 호준오빠 풀이
# sol1
def infix_to_postfix(expression):
    postfix = ""
    stack = []
    for exp in expression:
        if exp.isnumeric():
            postfix += exp
        else:
            if len(stack):
                postfix += stack.pop()
            stack.append(exp)
    while len(stack):
        postfix += stack.pop()
    return postfix

def eval_postfix(expression):
    stack = []
    for exp in expression:
        if exp.isnumeric():
            stack.append(int(exp))
        else:
            result = (stack.pop() + stack.pop())
            stack.append(result)
    return stack[0]

for tc in range(1, 11):
    _ = int(input())
    expression = input()
    expression_postfix = infix_to_postfix(expression)
    result = eval_postfix(expression_postfix)
    print(f'#{tc} {result}')

for t in range(10):
    _ = input()
    print(f'#{t+1}', sum(list(map(int, input().split('+')))))

# sol2
for t in range(10):
    _ = input()
    print(f'#{t+1}', sum(list(map(int, input().split('+')))))

# sol3
for t in range(10):
    input()
    print(f'#{t+1} {eval(input())}')