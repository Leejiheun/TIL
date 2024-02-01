T = int(input())  # 테스트 케이스의 수를 입력받습니다.
# 범위를 넘기는지, 1) 0이 아닌지점  2) 더이상 안넘어가는 지점
# 방향전환
for tc in range(1, T+1):  # 각 테스트 케이스에 대해
    N = int(input())  # 행렬의 크기 N을 입력받습니다.
    matrix = [[0] * N for _ in range(N)]  # N x N 크기의 행렬을 초기화합니다.
    direction = 0  # 초기 방향을 오른쪽으로 설정합니다.
    r = c = d = 0  # 현재 위치와 방향 전환을 위한 변수를 초기화합니다.
    for i in range(1, N ** 2 + 1):  # 1부터 N^2까지의 숫자에 대해 # 가장 마지막 숫자가 9,16...이여서 제곱 # 넣어줄 숫자를 반봅
        matrix[r][c] = i  # 현재 위치에 숫자를 채웁니다.
        # 방향 전환 조건을 확인하고 필요한 경우 방향을 전환합니다.
        if direction == 0 and c == N - 1 - d:  # 오른쪽 끝에 도달한 경우 # depth
        # if direction == 0 and (c == N-1 or matrix[r][c+1]):  # 오른쪽 끝에 도달한 경우 # depth
            direction = 1  # 아래로 방향 전환
        elif direction == 1 and r == N - 1 - d:  # 아래쪽 끝에 도달한 경우
        # elif direction == 1 and (r == N or matrix[r + 1][c + 1])
            direction = 2  # 왼쪽으로 방향 전환
        elif direction == 2 and c == 0 + d:  # 왼쪽 끝에 도달한 경우
            direction = 3  # 위로 방향 전환
        elif direction == 3 and r == 0 + d + 1:  # 위쪽 끝에 도달한 경우
            direction = 0  # 오른쪽으로 방향 전환
            d += 1  # 다음 레벨로 이동
        # 현재 방향에 따라 위치를 이동합니다.
        if direction == 0:  # 오른쪽으로 이동
            c += 1
        elif direction == 1:  # 아래로 이동
            r += 1
        elif direction == 2:  # 왼쪽으로 이동
            c -= 1
        elif direction == 3:  # 위로 이동
            r -= 1

    print(f'#{tc}')  # 테스트 케이스 번호를 출력합니다.
    for row in matrix:  # 각 행에 대해
        # print(*r, sep=' ')
        print(' '.join(map(str, row)))  # 행렬을 출력합니다.