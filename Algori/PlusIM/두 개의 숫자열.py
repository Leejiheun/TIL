testcase=int(input())

for tc in range(1,testcase+1):
    ans=0
    n,m=map(int,input().split())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))

    if n>m:  # 짧은 배열을 A로 만들기
        A,B=B,A
        n,m=m,n

    Sum=0
    Max=-21e8
    for i in range(0, m-n+1):
        Sum=0
        for j in range(n):  # n개 구간의 곱을 더한 값 구하기
            Sum+=(A[j] * B[i+j])
        Max=max(Max,Sum) # 안에있는 for문 끝나고 Max값 갱신하기

    ans=Max
    print(f'#{tc} {ans}')