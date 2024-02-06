T = int(input())
for tc in range(1, 1+T):
    N = input()
    M = input()
    if N in M:
        result = 1
    else:
        result =0
    print(f'#{tc} {result}')



def f(pat, txt, M, N):
    for i in range(N-M+1):
        for j in range(M):
            if txt[i+j] != pat[j]: # 불일치면 다음 시작 위치로 가고
                break
        else: # for문이 잘 끝났다면.. for else 문
            return 1
    return 0
T = int(input())
for tc in range(1, T+1):
    pat = input()
    txt = input()
    M = len(pat)
    N = len(txt)