T = 10
for tc in range(1, T+1):
    N = int(input())
    fx = input()
    st = []
    postfix = ''

    for tk in fx:
        if tk == '+':
            while st:
                postfix += st.pop()
            st.append(tk)
        elif tk == '*':
            if st and st[-1] == '*':
                st.append(tk)
            else:
                st.append(tk)
        else:
            postfix += tk
    while st:
        postfix += st.pop()

    for tk in postfix:
        if tk in '+*':
            t1 = st.pop()
            t2 = st.pop()
            if tk == '+':
                t3 = int(t1) + int(t2)
                st.append(t3)
            else:
                t3 = int(t1) * int(t2)
                st.append(t3)
        else:
            st.append(tk)
    print(f'#{tc} {st[0]}')

###########
# for x in range(10):
#     n = int(input())
#     st = []
#     postfix = ''
#     fx = input().strip()

#     for tk in fx:
#         if tk == '+':
#             while st:
#                 postfix += st.pop()
#             st.append(tk)
#         elif tk == '*':
#             if st and st[-1] == '*':
#                 postfix += st.pop()
#                 st.append(tk)
#             else:
#                 st.append(tk)
#         else:
#             postfix += tk
#     while st:
#         postfix += st.pop()
#     for tk in postfix:
#         if tk in '+*':
#             t1 = int(st.pop())
#             t2 = int(st.pop())
#             if tk == "+":
#                 t3 = int(t1) + int(t2)
#                 st.append(t3)
#             else:
#                 t3 = int(t1) * int(t2)
#                 st.append(t3)
#         else:
#             st.append(tk)
#     print(f'#{x + 1} {st[0]}')
    

#######보충
T = 10  # 테스트 케이스의 수
for tc in range(1, T+1):  # 각 테스트 케이스에 대해
    print(f'#{tc}', end=' ')  # 테스트 케이스 번호를 출력
    _ = input()  # 불필요한 입력은 무시
    cal = input()  # 수식을 입력받음
    st = []  # 스택을 초기화
    new_cal = ''  # 후위 표기법으로 변환된 수식을 저장할 변수
    for c in cal:  # 수식의 각 문자에 대해
        if c not in '+*':  # 숫자라면
            new_cal += c  # 후위 표기법 수식에 추가
        else:  # 연산자라면
            if not st:  # 스택이 비어있다면
                st.append(c)  # 연산자를 스택에 추가
                continue
            top = st[-1]  # 스택의 맨 위 요소를 확인
            if not (top == '+' and c == '*'):  # 우선순위를 고려하여
                while st and not (st[-1] == '+' and c == '*'):  # 스택에서 연산자를 꺼내 후위 표기법 수식에 추가
                    new_cal += st.pop()
            st.append(c)  # 현재 연산자를 스택에 추가
    while st:  # 스택에 남아있는 연산자를 모두 꺼내 후위 표기법 수식에 추가
        new_cal += st.pop()
    st.clear()  # 스택을 초기화
    for c in new_cal:  # 후위 표기법 수식의 각 문자에 대해
        if c not in '+*':  # 숫자라면
            st.append(int(c))  # 스택에 추가
        else:  # 연산자라면
            pop1 = st.pop()  # 스택에서 두 개의 숫자를 꺼내
            pop2 = st.pop()
            if c == '+':  # 덧셈이라면
                st.append(pop2 + pop1)  # 더한 결과를 스택에 추가
            else:  # 곱셈이라면
                st.append(pop2 * pop1)  # 곱한 결과를 스택에 추가
    print(st[-1])  # 스택의 맨 위에 있는 최종 결과를 출력