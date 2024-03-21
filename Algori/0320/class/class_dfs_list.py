# 인접 행렬 DFS : 재귀ver
graph =[
    [1, 3],
    [0, 2, 4],
    [1],
    [0, 4],
    [1, 3],
]

# stack으로 하는 방법도 있음
# 재귀로 구현

visited = [0] * 5
path = []

def dfs(now):
    # 기저 조건 (언제까지)
    # 지금 문제에서 없다!

    # 다음 재귀 호출 전
    # visited[now] = 1
    # path.append(now)

    # 다음 재귀 호출
    # 인접 리스트
    # 차이점 1. 갈 수 없는 조건 필요 없음
    # 차이점 2. for 문 작성
    for to in graph[now]:
        # 이미 방문했다면 pass
        if visited[to]:
            continue

        visited[to] = 1
        path.append(to)
        dfs(to)
    # 돌아왔을 때 작업

# 출발점 초기화
visited[0] = 1
path.append(0)
dfs(0)
print(path)



# graph =[
#     [1, 3],
#     [0, 2, 4],
#     [1],
#     [0, 4],
#     [1, 3],
# ]
#
# visited = [0] * 5
# path = []
#
# def dfs(now):
#     for to in graph[now]:
#         if visited[to]:
#             continue
#
#         visited[to] = 1
#         path.append(to)
#         dfs(to)
# visited[0] = 1
# path.append(0)
# dfs(0)
# print(path)