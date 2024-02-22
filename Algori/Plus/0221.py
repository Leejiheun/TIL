# 순회 중요
'''
전위 순회
중위 순회
후위 순회
+ 순회 방법
'''

# 사칙연산
# 수식 트리를 만들어줘야함
# 왼쪽 자식, 오른쪽 자식을 1차원 배열로 각각 만들어줌
# 완전이진트리가 아니라 2차원 배열로 못 함
T = 10
for tc in range(1, T+1):
    N = int(input())# 정점의 개수
    left = [0] * (N+1) # 왼쪽 자식에 대한 정점 번호 작성, 3번 정점에 2번 자식이 있다..# 정점이 1부터 시작하기 때문에
    right = [0] * (N+1) # 왼쪽 자식에 대한 정점 번호 작성, 3번 정점에 2번 자식이 있다..
    tree = [0] * (N+1) # 노드의 정보들을 tree 라는 이름으로 저장. 연산자, 피연산자를 직접기록해서 데이터 저장. 정점 i에 대해 데이터를 저장할 수 있는 배열
    # 정점의 갯수 만큼 정점의 정보를 받아보겠습니다.
    for i in range(N):
        # 연산자 : '1 - 2 3'
        # 피연산자 : '3 10'
        # 요소가 4개면 연산자, 요소가 2개면 피연산
        s = input().split()
        if len(s)==4: # 연산자
            tree[int(s[0])] = s[1]# 정점 1에 대해서 데이터가 '-'인 노드 .. 왼쪽 자식과 오른쪽 자식에 대한 정점 번호
            left[int(s[0])] = int(s[2])
            right[int(s[0])] = int(s[3])
        else: # 피연산
            tree[int(s[0])] = int(s[1]) # 정점 3에 대해서 데이터가 10인 노드

    # 로직 (수식 트리 -> 후위 표현식)
    # 후위표현식 -> 결과값 출력..! : 후위 순회가 진행되는 코드가 필요
    # 출력
    def post_order(v):
        if v == 0: # 기저조건
            return
        post_order(left[v]) # L
        post_order(right[v]) # R
        # v 자기자신방문
        # 현재 노드가 연산자이라면, 왼쪽 자식의 값과 오른쪽 자식의 값 갖고 연산 수행
        if tree[v] == '+':
            tree[v] = tree[left[v]] + tree[right[v]]
        elif tree[v] == '-':
            tree[v] = tree[left[v]] - tree[right[v]]
        elif tree[v] == '/':
            tree[v] = tree[left[v]] // tree[right[v]]
        elif tree[v] == '*':
            tree[v] = tree[left[v]] * tree[right[v]]
    post_order(1) # 루트노드 1에 대해서 후위순회...

    print(f'#{tc} {tree[1]}')