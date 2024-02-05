T = int(input())
for tc in range(1, 1+T):
    N = str(input())
    M = list(map(int, input().split()))
    if N in M:
        result = 1
    else:
        result =0
    print(f'#{tc} {result}')