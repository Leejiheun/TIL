for _ in range(10):
    tc = int(input())

    arr = [list(map(int, input().split())) for _ in range(100)]
    # 왼쪽, 오른쪽, 위쪽으로만 좌표 탐색을 통해 좌표의 값이 1인 경우를 찾아 이동
    di = [0, 0, -1]
    dj = [1, -1, 0]
    i, j = 99, arr[99].index(2)  # 2의 좌표

    while i != 0:
        if 0 <= i + di[0] <= 99 and 0 <= j + dj[0] <= 99 and arr[i + di[0]][j + dj[0]] == 1:
            arr[i][j] = 0  # 리스트에 새로운 요소 할당
            i = i + di[0]
            j = j + dj[0]
        elif 0 <= i + di[1] <= 99 and 0 <= j + dj[1] <= 99 and arr[i + di[1]][j + dj[1]] == 1:
            arr[i][j] = 0  # 리스트에 새로운 요소 할당
            i = i + di[1]
            j = j + dj[1]
        else:
            arr[i][j] = 0  # 리스트에 새로운 요소 할당
            i = i + di[2]
            j = j + dj[2]
    print(f'#{tc} {j}')

# ladder
# T = int(input())
# arr = [list(map(int, input().split())) for tc in range(100)]