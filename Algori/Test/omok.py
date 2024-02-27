def oMok(y, x):
    dy = [-1,1,0,1]
    dx = [1,0,1,1]

    for k in range(4):
        cnt = 0
        for l in range(5):
            dyy = i + dy[k] * l
            dxx = i + dx[k] * l
            
            if dxx<0 or dxx>=N or dyy < 0 or dyy >= N: break
            if arr[dyy][dxx] == 'o':
                cnt += 1
        if cnt == 5:
            return 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]
    flag = 0
    ans = 'No'
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                ret = oMok(i,j)
                if ret == 1:
                    flag = 1
                    ans = 'Yes'
                    break
        if flag == 1:
            break
    print(f'#{tc} {ans}')

                    