# 당근
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    cnt = 0
    max_n = 0
    for i in range(1,N):
        if arr[i] > arr[i-1]:
            cnt += 1
            if max_n < cnt:
                max_n = cnt
        else:
            cnt = 0
    ans = max_n + 1

    print(f'#{tc} {ans}')