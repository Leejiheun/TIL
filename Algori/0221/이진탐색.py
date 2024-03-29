# 강사님
T = int(input())  # 테스트 케이스의 수를 입력 받습니다.
for tc in range(1, T+1):  # 각 테스트 케이스에 대해
    print(f'#{tc}', end=' ')  # 테스트 케이스 번호를 출력합니다.
    N = int(input())  # 노드의 수를 입력 받습니다.

    cnt = 1  # 노드에 부여할 번호를 초기화합니다. 1번부터!

    tree = [0] * (N+1)  # 각 노드의 값을 저장할 배열을 초기화합니다.
    st = [1]  # 스택을 초기화하고 루트 노드를 추가합니다. 첫번쨰 노드부터 넣어줌
    order = []  # 중위 순회의 순서를 저장할 리스트를 초기화합니다.
    visited = [0] * (N+1)  # 각 노드의 방문 여부를 저장할 배열을 초기화합니다.
    while st:  # 스택이 비어있지 않는 동안
        node = st.pop()  # 스택에서 노드를 꺼냅니다.
        if (node*2 > N) or visited[node]:  # 노드가 리프 노드이거나 이미 방문한 노드인 경우
            order.append(node)  # 노드를 순서 리스트에 추가합니다.
            continue  # 다음 노드를 처리합니다.
        visited[node] = 1  # 노드를 방문했음을 표시합니다.

        if node*2+1 <= N:  # 노드의 오른쪽 자식이 있는 경우
            st.append(node*2+1)  # 오른쪽 자식을 스택에 추가합니다.
        st.append(node)  # 노드를 다시 스택에 추가합니다.
        if node*2 <= N:  # 노드의 왼쪽 자식이 있는 경우
            st.append(node*2)  # 왼쪽 자식을 스택에 추가합니다.
    for o in order:  # 중위 순회의 순서대로 각 노드에 대해
        tree[o] = cnt  # 노드에 번호를 부여합니다.
        cnt += 1  # 번호를 증가시킵니다.
    print(tree[1], tree[N//2])  # 루트 노드와 N/2번 노드의 값을 출력합니다.