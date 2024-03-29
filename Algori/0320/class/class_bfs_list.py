# 인접 행렬 BFS
graph =[
    [1, 3],
    [0, 2, 4],
    [1],
    [0, 4],
    [1, 3],
]
visited = [0] * 5

def bfs(start):

    # 시작 노드를 큐에 추가 + 방문 표시
    queue = [start]
    visited[start] = 1

    while queue: # 큐가 빌 때 까지
        now = queue.pop(0)
        print(now, end=' ')

        # 갈 수 있는 곳을 체크
        for to in graph[now]:
            if visited[to]:
                continue

            visited[to] = 1
            # print(visited)
            queue.append(to)
bfs(0)