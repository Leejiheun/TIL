def oMok(y,x):
        directy=[-1,1,0,1]
        directx=[1,0,1,1]

        for i in range(4): # 네 방향을 탐색 (1시 6시 3시 5시)
                cnt = 0
                for power in range(5): # 돌 5개를 탐색
                        dy=y+directy[i]*power
                        dx=x+directx[i]*power
                        if dy<0 or dy>=n or dx<0 or dx>=n: break #배열 범위 넘어가면 해당 방향 탐색 중지
                        if arr[dy][dx]=='o': # 돌의 개수 세기
                                cnt+=1
                if cnt==5: # 돌이 5개가 되어서 오목이라면
                        return 1 # 함수종료

testcase=int(input())
for tc in range(1,testcase+1):
        ans='NO'
        n=int(input())
        arr=[input() for _ in range(n)]
        flag=0
        for i in range(n):
                for j in range(n):
                        if arr[i][j]=='o': # 돌을 발견하였다면
                                ret=oMok(i,j) # 그부분부터 탐색 시작
                                if ret==1:
                                        flag=1 # 오목을 찾았을 경우
                                        ans='YES'
                                        break
                if flag==1: # 오목을 찾았으면 탐색 멈추기
                        break


        print(f'#{tc} {ans}')