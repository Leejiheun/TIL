# 백패킹 알고리즘 / A유형
# 2, 3 위치는 랜덤 / 스택형태로 풀어봄
T = int(input())
for tc in range(1, T+1):  # 각 테스트 케이스에 대해
    N = int(input())  # 보드의 크기를 입력받습니다.
    maze = [input() for _ in range(N)]  # 보드의 상태를 입력받습니다.
    result = 0  # 0을 기본값으로 두고 결과를 저장하는 변수를 초기화합니다. # 미로탐색에 성공하면 1을 할당하는 방식
    st = []  # 스택을 초기화합니다.

    for i in range(N):  # 보드의 각 위치에 대해
        for j in range(N):
            if maze[i][j] == '2':  # 시작 위치를 찾아 # 숫자로 안바꿔준상태라 문자열'2'로.
                st.append([i, j])  # 스택에 추가합니다. # (i, j) # 시작좌표를 i, j 쌍으로 넣어줌

    # 탐색 -> 재귀, BFS로도 가능한데, 지금은 스택으로!
    ## 특정 좌표 방문을 기록하는 리스트
    visited = [[0] * N for _ in range(N)]  # 방문 여부를 저장하는 2차원 리스트를 초기화합니다.
    di = [-1, 1, 0, 0]  # 상하좌우 이동을 위한 델타값을 설정합니다. # d = [(-1,0), (1,0), (0,-1), (0,1)]
    dj = [0, 0, -1, 1]  # 탐색 순서 조건 없으면 짝만맞다면 순서는 상관없음 # 가끔 시계방향,,등 조건있을 수 있음

    while st:  # 스택이 빌 때까지
        i, j = st.pop()  # 스택에서 위치를 꺼내 # (i, j)
        # i -> 행좌표, j -> 열 좌표
        visited[i][j] = 1  # 방문 표시를 합니다. # 방문 여부 체크
        for k in range(4):  # 상하좌우로 이동하며
            ni = i + di[k]
            nj = j + dj[k]
            # 미로 범위를 넘는지 확인 방법1
            if not (0 <= ni < N): # ni 좌표 검사
                continue
            if not (0 <= nj < N): # nj 좌표 검사
                continue
            if visited[ni][nj]: # 방문여부 검사
                continue # 이 반복 중지하고 다음 반복으로!
            # 0 or 1 or 3을 만난다
            # 0 : 이동 가능함
            if maze[ni][nj] == '0':
                st.append([ni, nj]) # 0
            # if maze[ni][nj] == 1:
            #     pass -> 하지 않음을 구현할 필요 없음
            if maze[ni][nj] == '3':
                result = 1
                st.clear() # 스택을 비워서 더이상 가망 없는 탐색 하지 않게함
                break # 델타(방향)에 대한 break
    print(f'#{tc} {result}')

            # # 미로 범위를 넘는지 확인 방법2
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]: # 보드 내에 있고 아직 방문하지 않은 위치라면
                if maze[ni][nj] == '0':  # 이동 가능한 위치라면
                    st.append((ni, nj))  # 스택에 추가합니다.
                if maze[ni][nj] == '3':  # 도착 위치라면
                    result = 1  # 결과를 1로 설정하고
                    st.clear()  # 스택을 비우며
                    break  # 반복문을 종료합니다.
    print(f'#{tc} {result}')  # 테스트 케이스 번호를 출력합니다.
