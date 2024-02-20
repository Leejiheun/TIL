# 0219 백준 문제
r = int(input())
N = list(map(int, input().split()))
T = int(input())
for _ in range(T):
    s = list(map(int, input().split()))
    if s[0] == 1:
        for n in range(len(N)):
            if (n+1) % s[1] == 0:
                if N[n] == 0:
                    N[n] = 1
                else:
                    N[n] = 0

    else:
        k = 1
        if N[s[1]-1] == 0:
            N[s[1]-1] = 1
        else:
            N[s[1]-1] = 0
        while 0 <= s[1]-1-k and s[1]-1+k < len(N) and N[s[1]-1-k] == N[s[1]-1+k]:
            if N[s[1]-1-k] == 0:
                N[s[1]-1-k] = 1
            else:
                N[s[1]-1-k] = 0
            if N[s[1]-1+k] == 0:
                N[s[1]-1+k] = 1
            else:
                N[s[1]-1+k] = 0
            k += 1

# 출력값 한 줄에 20개씩 출력하기
cnt = 0
for i in range(0, r):
    print(N[i], end=" ")
    cnt += 1
    if cnt == 20:
        cnt = 0
        print()