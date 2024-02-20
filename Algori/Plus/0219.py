# 완전 탐색 : 가능한 모든 경우의 수를 탐색하는 방법
# 완전탐색에서 제일 먼저 나오는 알고리즘은 Brute-Force 알고리즘
# 순열[1, 2, 3, 4]를 갖고 만들 수 있는 가짓수
'''
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            for l in range(1, 5):
                if i! = j and j! = k and k != l\
                and i != k and i == l and ...:
'''
# 어떻게 효율적으로 모든 경우를 탐색할 수 있는지 - 데이터의 형태를 파악!!

# 1. 선형적인 데이터를 띄우고 있는가..(배열)
# 2. 일대다(1:N) 의 형태 -> 트리
# 3. 다대다(N:M) 의 형태 -> 그래프 (완전탐색 = DFS, BFS..)
# - DFS : 깊이우선, 경로를 끝까지 탐색하고, *이전 경로로 돌아가서* 탐색을 수행
# => 스택(stack) : 되돌아갈 수 있는 노드 
# - BFS : 너비우선, 시작 노드를 기준으로 해서 *인접한* 노드를 차례대로 순회하는 방식으로 탐색
# => 큐(queue) : 내가 이접(방문할)노드

# 1226. 미로1
T = 10
N = 16
for _ in range(1, T+1):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    # 로직

    # 어떤 방법으로 완전탐색을 수행할까?
    # DFS, BFS, ... 
    # 델타 : 위아래왼오
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    # 이러한 완전 탐색에 사이클이 존재하는 경우는? -> 방문체크
    visited = [[False] * N for _ in range(N)] # 방문체크위한 배열    N*N
    
    # 도착지점에 도달한것 나타내는 변수 플래그
    goal_in = False
    def dfs(x, y) : # 재귀호충 방법 DFS...
        global goal_in
        # 기저 조건(종료조건) : 도착점에 도달했을 때
        if maze[x][y] == 3: # 도착지점에 도착했을 때, 종료
            goal_in = True
            return
        
        visited[x][y] = True # (x,y) 좌표에 대해서 방문체크..!
        # 자기 자신을 호출 (재귀호출)
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
    

            if nx < 0 or nx >= y or ny < 0 or ny >=N or maze[nx][ny] or visited[nx][ny]:
                continue
            if goal_in:  # 재귀호출을 덜 하면서 탐색을 진행 가능...!
                return
            dfs(nx, ny)
    # 출력
    # 도달이 가능함1, 도달이 불가능 0
    if goal_in:
        result = 1
    else:
        result = 0
        
    print(f"#{tc} {result}")