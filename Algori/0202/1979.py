# N = 5 (5*5) K = 3 (단어길이)
# 흰 1 검 0
# 흰색 부분에 단어가 들어감
# 1(흰색)이 가로로 N(3)개있을 때, 세로로 N개 있을 때
# T = int(input())
# N, K = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
# # 먼저, 가로에서 1이 연속으로 세개가 있는지 확인
# for i in range(N):
#     pass

# 수업시간강사님풀이

# 가로 또는 세로로 연속한 1의 개수가 k인 경우
# K = 3
# N = 7
# # 1이면 하나 증가, 0이면 초기화, 1이면 1증가, 1이면 1증가, 1이면 1증가
# # 근데 [0, 1, 1, 1, 1, 0] 이면..? 1이 연속 4개라 X, 딱 맞아 떨어지는 걸 찾아야함
# # 초기화 하기 전에 if count 하고 초기화
# cnt = 0
# ans = 0
# arr = [0, 1, 0, 1, 1, 1, 0]
# for i in range(N):
#     if arr[i] == 0:
#         if cnt == K:
#             ans += 1
#         cnt = 0
#     else: # arr[i] ==1
#         cnt += 1
#         # if i == N-1 and cnt == K:
#         #     ans += 1
# print(ans)

# 문제
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) + [0] for _ in range(N)] +[[0]*(N+1)] # 0 을 붙이는 방법
    N += 1 # N이 1이 커짐
    # 가로, 세로로 연속한 1의 개수가 K인 경우의 수
    ans = 0
    for i in range(N):
        cnt = 0 # i행에서 연속한 1의 개수
        for j in range(N):
            if arr[i][j]:
                cnt += 1
            else: # arr[i][j] == 0 이면
                if cnt == K:
                    ans += 1
                cnt = 0
    for j in range(N):
        cnt = 0 # i행에서 연속한 1의 개수
        for i in range(N):
            if arr[i][j]:
                cnt += 1
            else: # arr[i][j] == 0 이면
                if cnt == K:
                    ans += 1
                cnt = 0
    print(f'#{tc} {ans}')
