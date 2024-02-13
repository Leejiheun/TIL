T = int(input())
for tc in range(1, T+1):  # 각 테스트 케이스에 대해
    print(f'#{tc}', end=' ')  # 테스트 케이스 번호를 출력합니다.
    a = input().split()  # 공백으로 구분된 문자열을 입력받아 리스트로 변환합니다.
    st = []  # 스택을 초기화합니다.
    for v in a:  # 리스트의 각 요소에 대해 # 전달받은 계산식을 앞으로부터 탐색
        # if v.isnumeric():  # 요소가 숫자라면
        if v not in ['+', '-', '*', '/', '.']: # 이 다섯개에 해당하지 않으면 숫자
            st.append(int(v))  # 그대로 스택에 추가합니다. # 정수로 바꿔주고 append
        else:  # 요소가 연산자라면
            if v == '.': continue  # '.'은 무시합니다. # 종료 # break도 가능
            if len(st) < 2:  # 스택에 숫자가 2개 미만이라면 # 2개 미만이면 꺼낼게없음음
                print('error')  # 'error'를 출력하고
                break  # 반복문을 종료합니다.
            op1 = st.pop()  # 스택에서 두 개의 숫자를 꺼냅니다.
            op2 = st.pop()
            if v == '+':  # 연산자에 따라
                st.append(op2 + op1)  # 해당 연산을 수행하고 결과를 스택에 추가합니다.
            if v == '-':
                st.append(op2 - op1)
            if v == '*':
                st.append(op2 * op1)
            if v == '/':
                st.append(op2 // op1)  # 나눗셈은 정수 나눗셈으로 처리합니다.
    else:  # 모든 요소를 처리한 후
        print(st[0] if len(st) == 1 else 'error')
        # 스택에 숫자가 하나만 남아있다면 그것을 출력하고, 그렇지 않다면 'error'를 출력합니다.
        # 스택에 하나만 남아있어야함. st[0] or st[-1]