from collections import deque

T = int(input())

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# di = [-1, 1, 0, 0]
# dj = [0, 0, -1, 1]

for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    N = int(input())
    visited = [[0] * N for _ in range(N)]
    maze = [input() for _ in range(N)]
    start_i = start_j = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                start_i = i
                start_j = j
    qu = deque()
    qu.append((start_i, start_j, 0))
    answer = 0
    while qu:
        i, j, k = qu.popleft()
        if maze[i][j] == '3':  # 도착점에 도달하는 이동은 빼줘야함
            answer = k - 1
            qu.clear()
            break
        visited[i][j] = 1
        # for ii, jj in zip(di,dj): # d (튜플)
        for di, dj in d: # d (튜플)
            ni = i + di
            nj = j + dj
            if not (0 <= ni < N):
                continue
            if not (0 <= nj < N):
                continue
            if visited[ni][nj]:
                continue
            # 0이 벽인지 1이 벽인지
            # 내가 숫자변환을 했는지 안했는지...
            if maze[ni][nj] == '1':
                continue
            qu.append((ni, nj, k+1))
    print(answer)