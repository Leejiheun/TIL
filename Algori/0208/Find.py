# 1
def dfs(i, V): # 시작 i, 마지막 V
    visited = [0]*(V+1) # visited, stack 생성 및 초기화
    st = []
    visited[i] = 1 # 시작점 방문
    print(i) # 정점에서 할 일
    while True: #탐색
        for w in adjl[i]:# 현재 방문한 정점에 인접하고 방문안한 정정w가 있으면
            if visited[w] == 0:
                st.append(i) # push(i). i를 지나서
                i = w
                visited[i] = 1
                print(i)
                break # for w
        else: # for w, i 에 인접 정점이 없으면
            # 스택이 비어있지 않으면( 지나온 정점이 남아있으면 )
            if st : # top > -1
                i = st.pop()
            else: # 스택이 비어있으면(출발점에서 남은 정점이 없으면)
                break # while true
    return
'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
V, E = map(int, input().split())
arr = list(map(int, input().split()))

adjl = [[] for _ in range(V+1)] # adjl[i] 행에 인접인 정점번호
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjl[n1].append(n2)
    adjl[n2].append(n1) # 방향이 없는 경우
dfs(1, V)


# 2
# def dfs(i): # 시작 i, 마지막 V
#     visited[i] = 1 # 방문표시
#     print(i) # 출력
#     # i에 인접하고 방문안한 w가 있으면
#     for w in adjl[i]:
#         if visited[w] == 0:
#             dfs(w)
#
# V, E = map(int, input().split())
# arr = list(map(int, input().split()))
#
# adjl = [[] for _ in range(V+1)] # adjl[i] 행에 인접인 정점번호
# print('adjl', len(adjl))
# for i in range(E):
#     n1, n2 = arr[i*2], arr[i*2+1]
#     print('n2', n2)
#     adjl[n1].append(n2)
#     adjl[n2].append(n1) # 방향이 없는 경우
# visited = [0] * (V+1) # visited, stack 생성 및 초기화
# dfs(1)
# # print(adjl)