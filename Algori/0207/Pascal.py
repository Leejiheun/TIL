T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc}')
    arr = [[1] for _ in range(N)]
    if N > 1:
        arr[1].append(1)

    for i in range(2, N):
        for j in range(1, i):
            arr[i].append(arr[i-1][j-1]+arr[i-1][j])
        arr[i].append(1)
    for row in arr:
        print(*row)