T = 10
for tc in range(1, T+1):
    N = int(input())

    # 일차원 배열에 왼쪽 자식들, 오른쪽 자식들, 부모들
    left = [0] * (N + 1) # 0 번 인덱스 사용X
    right = [0] * (N + 1) # 오른쪽 자식
    parent = [0] * (N + 1) # 부모
    # 해당 정점 i의 데이터를 기록하는 배열 data
    data = [0] * (N + 1)

    # 각 정점 N개에 대한 정보들
    for _ in range(N):
        s = input().split()
        current = int(s[0]) # 부모 노드
        alphabet = s[1] # 데이터 알파벳
        
        # 자식이 두개 있는 경우
        if len(s) == 4:
            left_c = int(s[2]) # 왼쪽 자식
            right_c = int(s[3]) # 오른쪽 자식
            # 부모-자식 관계에서 부모를 기록
            parent[left_c] = current
            parent[right_c] = current

            left[current] = left_c # 왼쪽 자식 기록
            right[current] = right_c # 오른쪽 자식 기록
        
        # 자식이 하나만 있는 경우
        elif len(s) == 3:
            left_c = int(s[2]) # 왼쪽 자식
            parent[left_c] = current
            left[current] = left_c # 왼쪽 자식 기록
        # 현재 정점에 대한 값을 기록
        data[current] = alphabet 

    # 로직( 중위 순회 코드 )
    result = ''

    def in_order(i):
        global result
        # 기저조건(종료조건) : i노드가 존재하지 않을 때
        if i == 0 :
            return
        # 왼쪽 자식
        in_order(left[i])
        # 나 자신
        result += data[i]
        # 오른쪽 자식
        in_order(right[i])
    in_order(1)
    # 출력
    print(f'#{tc} {result}')

    # 수식트리, 이진탐색트리