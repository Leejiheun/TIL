testcase=int(input())
for tc in range(1, testcase+1):
    ans=0
    n,m=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(n)]
    Max=-21e8

    for _ in range(2):
        for i in range(n): # 열
            cnt=0
            for j in range(m): # 행
                if arr[i][j]==1: # 안의 값이 1일때
                    cnt+=1
                else: # 값이 0일떄
                    Max=max(Max,cnt)
                    cnt=0
            Max=max(Max,cnt)
        arr=list(map(list,zip(*arr)))
        n,m=m,n
    ans=Max
    print(f'#{tc} {ans}')