T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    Aj = list(map(int, input().split())) # 1 5 3 # N
    Bj = list(map(int, input().split())) # 3 6 -7 5 4 #M

    max_v = 0
    cnt = 0

    for i in range(M-N+1):
        cnt += Aj[i] * Bj[i]
        if max_v < cnt:
            max_v = cnt
    print(f'#{tc} {max_v}')