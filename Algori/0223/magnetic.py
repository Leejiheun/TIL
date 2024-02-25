T = 10  # 테스트 케이스의 수
N = 100  # 격자의 크기

def deadlock1():
    global cnt 
    for j in range(N): 
        i1 = -1
        while i1 < N - 1:
            i1 += 1
            if red[j] & (1 << i1): 
                for i2 in range(i1 + 1, N):  # 빨간색 사각형 아래의 줄에 대해
                    if blue[j] & (1 << i2):  # 파란색 사각형이라면
                        cnt += 1  # 카운터 증가
                        i1 = i2  # i1을 i2로 업데이트
                        break  # 루프 종료

def deadlock2():
    global cnt  # 전역 변수 cnt 사용
    for j in range(N):  # 각 열에 대해
        red_flag = False  # 빨간색 사각형 플래그 초기화
        for i in range(N):  # 각 줄에 대해
            if red_flag:  # 빨간색 사각형이 등장했다면
                if blue[j] & (1 << i):  # 파란색 사각형이라면
                    red_flag = False  # 빨간색 사각형 플래그 초기화
                    cnt += 1  # 카운터 증가
            else:
                if red[j] & (1 << i):  # 빨간색 사각형이라면
                    red_flag = True  # 빨간색 사각형 플래그 설정

for tc in range(1, T+1):  # 각 테스트 케이스에 대해
    print(f'#{tc}', end=' ')  # 테스트 케이스 번호를 출력
    _ = input()  # 테스트 케이스 정보를 입력 받음 (이 경우 사용하지 않음)
    red = [0] * N  # 빨간색 사각형의 위치를 저장할 배열
    blue = [0] * N  # 파란색 사각형의 위치를 저장할 배열
    for i in range(N):  # 각 줄에 대해
        row = input()  # 줄을 입력 받아 공백으로 분리
        for j in range(N):  # 각 열에 대해
            if row[j * 2] == '1':  # 빨간색 사각형이라면
                red[j] |= 1 << i  # 해당 위치에 빨간색 사각형 표시
            if row[j * 2] == '2':  # 파란색 사각형이라면
                blue[j] |= 1 << i  # 해당 위치에 파란색 사각형 표시
    cnt = 0  # 카운터 초기화
    # deadlock1()  # deadlock1 함수 호출 (현재 주석 처리됨)
    deadlock2()  # deadlock2 함수 호출
    print(cnt)  # 빨간색 사각형 위에 있는 파란색 사각형의 개수를 출력