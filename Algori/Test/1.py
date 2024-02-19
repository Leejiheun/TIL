# 0219 백준 문제
_ = input()
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
        print(N)
    if s[0] == 2:
        for k in range(1, 101):
            while N[s[1]-1]-k != N[s[1]-1]+k:
                if N[s[1]-1]-k == N[s[1]-1]+k:
                    if N[n] == 0:
                        N[n] = 1
                    else:
                        N[n] = 0
            print(N)


    # while N(s[1]-1) :
    # # if N[s[1]-1] == 0 and N[s[1]-2] == N[s[1]] and N[s[1]-3] == N[s[1]+1]:
    #     print(N[s[1] - 1] == 1 and N[s[1]-2] == N[s[1]] == 0 and N[s[1]-3] == N[s[1]+1] == 1)