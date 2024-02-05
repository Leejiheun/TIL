T = int(input())
for tc in range(1, 1+T):
    N = str(input())
    M = list(map(int, input().split()))
    if N in M:
        print(1)
    else:
        print(0)