# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split()) # 크기 # 개수
#     Ci = input().split() # 치즈양
#     pass
from collections import deque

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    N, M = map(int, input().split())
    pizzas = list(map(int, input().split()))
    # 인덱스를 원형큐에 넣는 방식으로
    # -> 피자의 치즈양을 조회할 때 인덱스로
    numbers = range(M)  # 피자의 번호 0 ~ M-1
    # 마지막에는 +1을 해줘야함.
    q = deque(numbers[:N]) # 0 ~ N-1
    # 7 2 6 5 3
    end = N-1 # 화덕에 들어간 가장 뒤에 있는 피자 인덱스
    while len(q) > 1: # q, st -> 아예 비었나, 뭐라도 있나
        front = q.popleft()  # 피자의 인덱스
        pizzas[front] //=2  # 치즈를 반으로 줄임
        # if pizzas[front] > 0:
        if pizzas[front]:  # 아예 0인지(False) 아닌지
            # 치즈가 남은 경우
            q.append(front)
        else : # pizzas[front] == 0  # 피자를 빼내야...
            if end < M - 1: # M -> M-1
                # 아직 들어갈 피자가 남았다
                end += 1
                q.append(end) #
    print(q[0]+1)  # 마지막 인덱스 조정.