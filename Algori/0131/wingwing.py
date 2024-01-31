# 중요문제!!
T = int(input())  # 테스트 케이스의 수를 입력받습니다.
for t in range(T):  # 각 테스트 케이스에 대해
    N, M = map(int, input().split())  # 행렬의 크기 N과 부분 행렬의 크기 M을 입력받습니다.
    matrix = [list(map(int, input().split())) for _ in range(N)]  # N x N 크기의 행렬을 입력받습니다. # for문으로 append도 괜찮
    sum_matrix = [[0] * (N - M + 1) for _ in range(N - M + 1)]  # 부분 행렬의 합을 저장할 행렬을 초기화합니다.
    for i in range(len(sum_matrix)):  # 각 행에 대해
        for j in range(len(sum_matrix)):  # 각 열에 대해
            # 해당 위치에서 시작하는 M x M 크기의 부분 행렬의 합을 계산하고 저장합니다.
            sum_matrix[i][j] = sum([
                sum(row[j:j+M])
                for row in matrix[i:M+i]]) # 하나의 박스 안에 네개가 있는 형태
            # i부터 m+i까지 행/ j부터 j+m 까지 열
            # 컴프리핸션 헷갈리면 지피티에게 일반적인 반복문으로 풀어달라고 요청! / 직관적인 반복문과 조건문으로 바꿔줘 도움 받기

    # 부분 행렬의 합 중 최대값을 찾아 출력합니다.
    print(f'#{t+1} {max([max(r) for r in sum_matrix])}')
    # max(map(max, matrix))