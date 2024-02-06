T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(8)]
    cnt = 0

    for i in range(8):
        for j in range(8 - N + 1):
            temp = arr[i][j:j+N]
            if temp == temp[::-1]:
                cnt += 1

    for j in range(8):
        for i in range(8 - N + 1):
            temp = []
            for k in range(i, i+N):
                temp.append(arr[k][j])
            if temp == temp[::-1]:
                cnt += 1
    print(f'#{tc} {cnt}')