T = int(input())
for tc in range(1, T+1):
    ans = 0

    n = int(input()) # 당근 개수
    lst = list(map(int, input().split()))
    cnt = 0 # 당근이 커진 횟수
    Max = 0 # 커진 횟수의 최댓값
    
    for i in range(1, n):
        if lst[i] > lst[i-1]:
            cnt += 1 # 당근이 커진 횟수 1 증가
            if Max < cnt:
                Max = cnt
        else:
            cnt = 0
    ans = Max + 1 # 당근이 커진 횟수 +1 -> 커진 당근의 개수

    print(f'#{tc} {ans}')