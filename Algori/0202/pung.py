di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    for i in range(N):
        for j in range(M):
            cnt = arr[i][j]
            for k in range(4):
                for l in range(1, arr[i][j]+1): # 4번돌면 중앙값에서 1만큼 상하좌우 더하고 그다음은 중앙에서 2만큼 떨어진 상하좌우 합,,,,
                    ni = i + di[k] * l
                    nj = j + dj[k] * l
                    if 0 <= ni < N and 0 <= nj < M:
                        cnt += arr[ni][nj]
            if max_v < cnt: # 꽃가루를 최대값과 비교
                max_v = cnt
    print(f'#{tc} {max_v}')


T = int(input())
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

di = [0,1,0,-1]
dj = [1,0,-1,0]

for tc in range(1, T+1):
    max_num = 0
    for i in range(N):
        for j in range(M):
            cnt = arr[i][j]
            for d_i in range(4):
                for d_j in range(4):
                    d_i = i + di[d_i]
                    d_j = j + dj[d_j]
                    if 0 <= d_i < N and 0 <= d_j < M:
                        cnt += arr[d_i][d_j]
            if max_num < cnt:
                max_num = cnt
    print(f'#{tc} {max_num}')