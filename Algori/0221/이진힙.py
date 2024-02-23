T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 노드 개수
    nodes = list(map(int, input().split()))
    item = [0] * (N+1) # 노드에 들어있는 값들
    # last = 0 # 마지막 노드 번호
    for i in range(1, N+1):
        item[i] = nodes[i-1]
        # 트리의 값을 나타내는 item 에 맨끝에 node 추가
        for j in range(i, -1, -1): # 역으로 가는거
            if item[j // 2] > item[j]: # 부모 노드의 위치를 가져오는 것
                item[j//2], item[j] = item[j], item[j//2]

    ancestor_sum = 0
    parent_node = N//2 # N에 대해 조상노드를 할 껀데, N//2 가 0이 될 때 까지,
    while parent_node > 0:
        ancestor_sum += item[parent_node]
        parent_node //= 2 # 루트 노드를 만날 때 까지
    print(ancestor_sum)

    '''
    ancestor = []  # 조상 노드들의 번호를 저장할 리스트를 초기화합니다.
    tmp = N // 2  # 마지막 노드의 부모 노드의 번호를 저장합니다.
    while tmp != 0:  # 루트 노드에 도달할 때까지
        ancestor.append(tmp)  # 조상 노드의 번호를 리스트에 추가합니다.
        tmp //= 2  # 부모 노드의 번호를 업데이트합니다.
    print(sum([item[v] for v in ancestor]))  # 조상 노드들의 값을 합산하여 출력합니다.
    '''