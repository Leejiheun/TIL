# 풍선팡, 풍선팡2, 파리퇴치
# 풍선팡2

# 풍선팡2
T = int(input())
di = [-1,1,0,0]
dj = [0,0,-1,1]
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0
    for i in range(N):
        for j in range(M):
            cnt = arr[i][j]
            for k in range(k):
                d_i = i+di[k]
                d_j = j+dj[k]
                if 0 <= d_i < N and 0 <= d_j < M:
                    cnt += arr[d_i][d_j]
            if max_v < cnt:
                max_v = cnt
    print(f'#{tc} {max_v}')

# 풍선팡
T = int(input())
di = [-1,1,0,0]
dj = [0,0,-1,1]
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0
    for i in range(N):
        for j in range(M):
            cnt = arr[i][j]
            for k in range(4):
                for l in range(1, arr[i][j]+1):
                    d_i = i + di[k] * l
                    d_j = j + dj[k] * l
                    if 0 <= d_i < N and 0 <= d_j < M:
                        cnt += arr[d_i][d_j]
            if max_v < cnt:
                max_v = cnt
    print(f'#{tc} {max_v}')

# 파리퇴치
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            cnt = 0
            for di in range(M):
                for dj in range(M):
                    cnt += arr[i+di][j+dj]
            if max_v < cnt:
                max_v = cnt
    print(f'#{tc} {max_v}')