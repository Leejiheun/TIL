T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    N, M, L = map(int, input().split())

    # parent = [0 for _ in range(0, N+1)]
    # for i in range(2, len(parent)):
    #     parent[i] = i // 2
    # 시작지점은 체크. 왜? 0번째 노드가 있을 수도...
    parent = [i // 2 for i in range(0, N+1)]

    # tree = [0 for _ in range(0, N+1)]  # 0~N
    tree = [0] * (N+1)
    for _ in range(M):  # 리프노드의 개수만큼
        n, v = map(int, input().split())
        tree[n] = v
    for i in range(N, 0, -1):
        if tree[i]: continue  # 값이 이미 존재한다면 리프노드
        for j in range(len(parent)):
            # 각 노드의 부모노드를 값으로 가진 리스트를 탐색
            if i == parent[j]: # 부모 노드와 현재 노드가 같다
                tree[i] += tree[j]  # 자식 노드의 값을 부모 노드에 더하기
    print(tree[L])