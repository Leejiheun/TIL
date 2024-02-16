T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    J = input().split()
    for _ in range(M):
        J.append(J.pop(0)) # popleft() 똑같음, 시간복잡도 다름
    print(f'#{tc}', J[0])

# 강사님 풀이
from collections import deque

T = int(input())  # 테스트 케이스의 수를 입력 받음

for tc in range(1, T+1):  # 각 테스트 케이스에 대해
    print(f'#{tc}', end=' ')  # 테스트 케이스 번호 출력
    N, M = map(int, input().split())  # 큐의 크기(N)와 회전 횟수(M)를 입력 받음
    arr = deque(input().split())  # 큐의 초기 상태를 입력 받음
		# print(arr[M % N]) # 나머지 연산을 활용한 풀이
    for _ in range(M):  # M번 회전
        arr.append(arr.popleft())  # 큐의 맨 앞 요소를 맨 뒤로 이동(enqueue 후 dequeue)
    print(arr[0])  # 회전 후 큐의 맨 앞 요소를 출력