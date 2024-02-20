T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N-M+1):
        for j in range(N-M+1):
            