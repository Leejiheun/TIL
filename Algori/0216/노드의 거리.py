# 인접 행렬 사용
def bfs(s, N, G): # 시작정점 s, 노드개수 N
    q = []                  # 큐 생성
    visited = [0] * (N+1)   # visited
    q.append(s)             # 시작점 인큐
    visited[s] = 1          # 시작점 방문표시(인큐 표시)
    while q:                # 처리안된 정점이 남아있으면,,
        t = q.pop(0)        # 처리할 정점 디큐
        if t == G:
            return visited[t]-1 # 최단 경로 간선 수(몇개의 간선이 지나가니?는 -1 하기)
        for i in adjl[t]:   # t에 인접인 정점이
            if visited[i] ==0:  # 인큐되지 않았으면(처리된적이 없으면)방문하지 않은 정점이면
                q.append(i)     # 인큐
                visited[i] = visited[t] + 1 # 방문표시
    return 0        # G까지 경로가 없는 경우

T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    adjl = [[] for _ in range(V+1)]
    for i in range(E):
        n1, n2 = map(int, input().split())
        adjl[n1].append(n2)
        adjl[n2].append(n1)
    S, G = map(int, input().split())

    print(f'#{tc+1} {bfs(S, V, G)}')



# 강사님 풀이
# 미로 찾기 등 '찾기' '길'이 나오면 델타 생각하기.
from collections import deque

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int, input().split())
        adj[s][e] = 1
        adj[e][s] = 1  # 양방향
    S, G = map(int, input().split())
    visited = [0] * (V+1)
    qu = deque()
    qu.append((S, 0))
    answer = 0
    while qu:  # 큐가 빌때까지
        node, distance = qu.popleft()
        if node == G:  # G - Goal
            answer = distance
            qu.clear()
            break
        if visited[node]:
            continue
        visited[node] = 1
        for i in range(1, V+1):
            if not adj[node][i]:
                continue
            qu.append((i, distance+1))
    print(f'#{tc} {answer}')