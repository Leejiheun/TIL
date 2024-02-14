T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    V, E = map(int, input().split())
    edges = [[0] * (V+1) for v in range(V+2)]

    for _ in range(E):
        start, end = map(int, input().split())
        edges[start][end] = 1

    S, G = map(int, input().split())
    result = 0
    st = [S]

    while st:  # 스택이 비어있지 않는 동안
        node = st.pop()  # 스택에서 정점을 하나 꺼냅니다.
        for i in range(V+1):  # 모든 정점에 대해
            if edges[node][i]:  # 해당 정점으로 이어진 간선이 있다면
                if i == G:  # 그 정점이 목표 정점이라면
                    break  # 반복문을 종료합니다.
                st.append(i)  # 그렇지 않다면 그 정점을 스택에 넣습니다.
        if i == G:  # 목표 정점에 도달했다면
            result = 1  # 결과를 1로 설정하고
            break  # 반복문을 종료합니다.
    print(result)  # 결과를 출력합니다.