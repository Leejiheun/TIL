def oMok(y,x):
        directy=[-1,1,0,1]
        directx=[1,0,1,1]

        for i in range(4):
                cnt = 0
                for power in range(5):
                        dy=y+directy[i]*power
                        dx=x+directx[i]*power
                        if dy<0 or dy>=n or dx<0 or dx>=n: break
                        if arr[dy][dx]=='o':
                                cnt+=1
                if cnt==5:
                        return 1

testcase=int(input())
for tc in range(1,testcase+1):
        ans='NO'
        n=int(input())
        arr=[input() for _ in range(n)]
        flag=0
        for i in range(n):
                for j in range(n):
                        if arr[i][j]=='o':
                                ret=oMok(i,j)
                                if ret==1:
                                        flag=1
                                        ans='YES'
                                        break
                if flag==1:
                        break


        print(f'#{tc} {ans}')