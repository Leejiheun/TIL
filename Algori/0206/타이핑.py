# asasa일 경우 asa라면 count쓰면 안되는 이유
# -> 앞 0:2에서 asa 와 뒤 2:4에 asa 두번이 세어짐
# Bf 적용하는 방법
T = int(input())

def bf(A, B):
    # A는 전체 텍스트 B는 탐색할 패턴
    len_A = len(A)
    len_B = len(B)
    i = j = 0 # 전체, 패턴 인덱스
    count = 0 # 버튼 누르는 횟수
    while i < len_A and j < len_B:
        if A[i] != B[j]:
            i -= j # j가 왜 -1이 아닌지
            j = -1 # 왜 0으로 안하냐면 뒤에 +1 할 거니깐
        i += 1
        j += 1
        if j == len_B:
            count += 1
            # i 와 j 에 아무것도 안해줌 -> 이전으로 돌아가지 않음
            # i는 건들 필요 없고 j만 0으로 만들어주면 됨
            j = 0 # 지금까지 탐색에 i 인덱스는 더이상 타자를 칠 대상 아님
    return len_A - count * (len_B -1)

for tc in range(1, T+1):
    # A가
    A, B = input().split() # 문자열이라 쪼개기만 하면 됨. map안해도 되는 이유
    result = bf(A,B)
    print(f'#{tc} {result}')







T = int(input())

def bf(A, B):
    # A는 전체 텍스트 B는 탐색할 패턴
    len_A = len(A)
    len_B = len(B)
    i = j = 0 # 전체, 패턴 인덱스
    count = 0 # 버튼 누르는 횟수
    while i < len_A and j < len_B:
        if A[i] != B[j]:
            i -= j # j가 왜 -1이 아닌지
            j = -1 # 왜 0으로 안하냐면 뒤에 +1 할 거니깐
        i += 1
        j += 1
        if j == len_B:
            count += 1
            # i 와 j 에 아무것도 안해줌 -> 이전으로 돌아가지 않음
            # i는 건들 필요 없고 j만 0으로 만들어주면 됨
            j = 0 # 지금까지 탐색에 i 인덱스는 더이상 타자를 칠 대상 아님
    return len_A - count * (len_B -1)

T = int(input())
for tc in range(1, T+1):
    # A가
    A, B = input().split() # 문자열이라 쪼개기만 하면 됨. map안해도 되는 이유
    result = 0
    while B in A:
        A = A.replace(B, '_')
    result = len(A)
    print(f'#{tc} {result}')