T = int(input())  # 테스트 케이스의 수를 입력받는다

def permutation2(x, depth):
    # x는 현재 노드의 위치, depth는 순열의 깊이(노드의 수)
    if x == depth:  # 모든 노드를 방문했다면
        cum_sum = 0  # 경로의 총 비용을 저장할 변수를 초기화한다
        for p in range(len(path_fixed) - 1):  # 경로의 각 노드에 대해
            start = path_fixed[p] - 1  # 시작 노드를 설정한다
            end = path_fixed[p + 1] - 1  # 종료 노드를 설정한다
            cum_sum += matrix[start][end]  # 시작 노드와 종료 노드 사이의 비용을 더한다
        global min_val  # 전역 변수 min_val을 사용한다
        min_val = min(cum_sum, min_val)  # 계산된 비용과 현재의 최소 비용을 비교하여 최소 비용을 갱신한다
        return
    for i in range(2, N+1):  # 각 노드에 대해
        if i in path_fixed: continue  # 이미 방문한 노드는 건너뛴다
        path_fixed[x] = i  # 노드를 방문한다
        permutation2(x+1, depth)  # 다음 노드를 방문한다
        path_fixed[x] = 0  # 노드 방문을 취소한다 (백트래킹)

def permutation(x):  # x는 현재 노드의 위치
    if x == N-1:  # 모든 노드를 방문했다면
        path2 = [1] + path + [1]  # 시작점과 종료점을 추가한다
        cum_sum = 0  # 경로의 총 비용을 저장할 변수를 초기화한다
        for p in range(len(path2) - 1):  # 경로의 각 노드에 대해
            start = path2[p] - 1  # 시작 노드를 설정한다
            end = path2[p+1] - 1  # 종료 노드를 설정한다
            cum_sum += matrix[start][end]  # 시작 노드와 종료 노드 사이의 비용을 더한다
        global min_val  # 전역 변수 min_val을 사용한다
        min_val = min(cum_sum, min_val)  # 계산된 비용과 현재의 최소 비용을 비교하여 최소 비용을 갱신한다
        return
    for i in range(2, N+1):  # 각 노드에 대해
        if i in path: continue  # 이미 방문한 노드는 건너뛴다
        path.append(i)  # 노드를 방문한다
        permutation(x+1)  # 다음 노드를 방문한다
        path.pop()  # 노드 방문을 취소한다 (백트래킹)

for tc in range(1, T+1):  # 각 테스트 케이스에 대해
    print(f'#{tc}', end=' ')
    N = int(input())  # 노드의 수를 입력받는다
    matrix = [list(map(int, input().split())) for _ in range(N)]  # 비용 행렬을 입력받는다
    path = []  # 방문 경로를 저장하는 리스트를 초기화한다
    path_fixed = [0] * (N+1)  # 방문 경로를 저장하는 리스트를 초기화한다 (백트래킹용)
    path_fixed[0] = 1  # 시작점을 설정한다
    path_fixed[N] = 1  # 종료점을 설정한다
    min_val = 100 * (N-1)  # 최소 비용을 초기화한다
    permutation2(1, N)  # 순열 생성을 시작한다
    print(min_val)  # 최소 비용을 출력한다