'''
간선의 개수를 최소화, 모든 정점을 연결하는 방법
1. 여러 가지 방법이 있다.
2. 싸이클이 발생하지 않는다.
3. 간선의 개수 : (V-1)개
=> 신장 트리

최소 비용 신장 트리
=> 그 중에 비용의 합이 제일 적은 신장 트리

1. 완탐 고려 : 모든 신장 트리를 구하자 => 시간적으로 많이 걸림
2. backtracking
3. DP, 그리디 등등,,
'''

# ptim 알고리즘
# 최소비용 : queue, 힙,,사용


'''
간선수 : 7-11
노드수 8개
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46 
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''
# 우선순위 큐를 활용
from heapq import heappush, heappop

def prim(start):
    pq = [] 
    MST = [0] * V

    # 최소 비용
    sum_weight = 0

    # 시작점 추가
    # [기존BFS] 노드 번호만 관리
    # [PRIM] 가중치가 낮으면 먼저 나와야 한다.
    # -> 관리해야할 데이터 : 가중치, 노드 번호 2가지
    # -> 동시에 두 가지 데이터 다루기
    #   1. class 로 만들기
    #   2. 튜플로 관리
    # 이차원 배열 + 가중치 + 높이
    heappush(pq, (0, start))

    while pq:
        weight, now = heappop(pq)

        # 우선순위 큐의 특성 상
        # 더 먼거리로 가는 바법이 큐에 저장이 되어 있기 때문에
        # 기존에 이미 더 짧은 거리로 방문했다면, continue
        
        if MST[now]:
            continue

        # 방문 처리
        MST[now] = 1
        # 누적합 추가
        sum_weight += weight

        # 갈 수 있는 노드들을 보면서
        for to in range(V):
            # 갈 수 없거나 이미 방문했다면 pass
            if graph[now][to] == 0:
                continue

            heappush(pq, (graph[now][to], to))
    print(f'최소 비용 : {sum_weight}')

V, E = map(int, input().split())
# 인접 행렬
# - [과제] 인접 리스트로 저장
graph = [[0] * V for _ in range(V)]
for _ in range(E):
    s, e, w = map(int, input().split())

# [기존] graph[3][4] = 1 3에서 4로 이동 가능
# [가중치 그래프] graph[3][4] = 31 3에서 4로 이동하는데 31 가중치(비용)이 든다
    graph[s][e] = w
    graph[e][s] = w