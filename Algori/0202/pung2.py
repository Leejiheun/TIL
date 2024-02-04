# pang2
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0 # 최대 꽃가루 합계

    for i in range(N): # N * M 크기의 게임판 # 행
        for j in range(M): # 열
            cnt = arr[i][j] # 터트린 풍선의 꽃가루 수 # 중앙값
            for k in range(4): # 주변 풍선의 인덱스 ni, nj /
                # 첫번째 돌면 오른쪽꺼 저장, 두번째 밑에꺼 누적 합, 세번째..좌,,네번쨰 상...
                ni = i + di[k] # 0
                nj = j + dj[k] # 1
                if 0 <= ni < N and 0 <= nj < M:
                    cnt += arr[ni][nj]
            if max_v < cnt: # 꽃가루 최대값과 비교
                max_v = cnt
    print(f'#{tc} {max_v}')

# pang
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