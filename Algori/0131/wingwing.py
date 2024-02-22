# 중요문제!!
T = int(input())  # 테스트 케이스의 수를 입력받습니다.
for t in range(T):  # 각 테스트 케이스에 대해
    N, M = map(int, input().split())  # 
    # 행렬의 크기 N과 부분 행렬의 크기 M을 입력받습니다.
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



# 중요문제!!
T = int(input()) 
for t in range(T):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    sum_matrix = [[0] * (N - M + 1) for _ in range(N - M + 1)]

    for i in range(len(sum_matrix)): # 0, 1, 2, 3
        for j in range(len(sum_matrix)): # 0, 1, 2, 3
            sum_matrix[i][j] = sum([
                sum(row[j:j+M]) # 0, 1
                for row in matrix[i:M+i]]) 
   
    print(f'#{t+1} {max([max(r) for r in sum_matrix])}')
    # max(map(max, matrix))


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    matric = [list(map(int, input().split())) for _ in range(N)]
    max_catch = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            catch_flies = 0

            for d_i in range(M):
                for d_j in range(M):
                    catch_flies += matric[i+d_i][j+d_j]

            if max_catch < catch_flies:
                max_catch = catch_flies
 
    print(f'#{tc} {max_catch}')


T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    matric = [list(map(int, input().split())) for _ in range(N)]
    max_num = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            catch = 0
            for n_i in range(M):
                for n_j in range(M):
                    catch += matric[i+n_i][j+n_j]
            if max_num < catch:
                max_num = catch
    print(f'#{tc} {max_num}')



T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    matric = [list(map(int, input().split())) for _ in range(N)]
    
    max_val = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            catch = 0

            for d_i in range(M):
                for d_j in range(M):
                    catch += matric[i+d_i][j+d_j]
            if max_val < catch:
                max_val = catch
    print(f'#{tc} {max_val}')