from collections import deque

T = int(input())
for tc in range(1, T+1):
    print('#', tc, sep='', end=' ')
    E, N = map(int, input().split())
    edges = list(map(int, input().split()))
    tree = [[] for _ in range(E+2)]
    # 1 ~ E+1 -> 0 ~ E+1.
    for i in range(0, len(edges), 2):
        # 2씩 증가 -> i. i번째 노드 번호,
        # i+1 연결된 하위 노드
        tree[edges[i]].append(edges[i+1])

    st = deque()
    st.append(N)
    cnt = 0
    while st:
        cnt += 1
        node = st.pop()
        for child in tree[node]:
            st.append(child)
    print(cnt)