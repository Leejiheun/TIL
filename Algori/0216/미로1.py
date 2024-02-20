# 인접행렬 X, 2차원 배열
T = 10
for tc in range(T):
    _ = int(input())

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    
    arr = [input() for i in range(16)]

    visited = [[0] * 16 for _ in range(16)]  # visited
    q = []  # 큐 생성
    q.append([1, 1])  # 시작점 인큐

    result = 0

    while q:    # 처리안된 정점이 남아있으면,,
        t = q.pop(0)
        for k in range(4):
            ni = t[0] + di[k]
            nj = t[1] + dj[k]
            if arr[ni][nj] == '0' and visited[ni][nj] == 0:
                q.append([ni, nj])  # 인큐
                visited[ni][nj] = 1  # 방문표시
            if arr[ni][nj] == '3':
                result = 1
                break

    print(f'#{tc+1} {result}')