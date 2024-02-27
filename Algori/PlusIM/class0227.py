# 몸풀기 문제 1
# 0 1 2 3 4 5 4 3 2 1 0

# def abc(level):
#     print(level,end=' ')
#     if level==5:
#         return
#
#     abc(level+1)
#     print(level, end=' ')
#
# abc(0)
###########################################
# 누적합 구하기 (재귀)
arr=[3,4,5,1,6,9]

# def abc(level, Sum):   # 1 Sum 매개변수 (지역변수)
#     print(Sum,end=' ')
#
#     if level==5:
#         return
#     abc(level+1,Sum+arr[level+1])
#
#     print(Sum,end=' ')
#
# abc(0,arr[0]) # level Sum




# 
# arr=[3,4,5,1,6,9]
# 
# Sum=arr[0] # 전역(글로벌) 변수
# 
# def abc(level):
#     global Sum
#     print(Sum, end=' ')
# 
#     if level==5:
#         return
#     Sum+=arr[level+1]
#     abc(level+1)
#     Sum-=arr[level+1]
# 
#     print(Sum,end=' ')
# 
# abc(0)  # level

# 재귀 또는 DFS 구현시 변수를 어떻게 선언 했는가에 따라서
# return 후 값을 원상복구 해야 하는 경우가 있고
# 원상복구 하지 않아도 괜찮은 경우가 있음
# 예> 누적합 구하는 Sum 변수를 매개변수로 활용시 원상복구 필요 없지만
# 전역변수로 sum을 선언시 함수 return 후 값을 다시 뺴 줘야 함 !!!

# 순열
# LEVEL BRANCH 정해지면 .. -> 코드로 구현이 가능!!!

people=[1,2,3,4]
used=[0]*4
path=[0]*3

def abc(level):

    if level==3:
        for i in range(3):
            print(path[i],end=' ')
        print()
        return

    for i in range(4):
        if used[i]==1: continue
        path[level]=i+1
        used[i]=1
        abc(level+1)
        used[i]=0


abc(0)



# 최소 동전 사용 개수
n=int(input()) # 거슬러 줄돈
coin=[110,70,10]
Min_coin=21e8 # 최소 동전으 개수 저장


def DFS(level,sum):
    global Min_coin
    if level==50:
        return

    if sum>n: # 누적합 > 거슬러 줄 돈보다 크다면
        return
    if level>Min_coin: # 최소 동전 사용 개수보다 더 들어갈 필요가 없음
        return
    if n==sum:# 거슬러 줄돈 n == 누적합
        Min_coin=min(Min_coin,level)# 최소 동전으 개수 갱신
        return

    for i in range(3):
        DFS(level+1,sum+coin[i])

DFS(0,0)  # LEVEL SUM
print(Min_coin)

# 전역 변수 사용
n=int(input()) # 거슬러 줄돈
coin=[110,70,10]
Min_coin=21e8 # 최소 동전으 개수 저장

sum=0
def DFS(level):
    global Min_coin,sum
    if level==50:
        return

    if sum>n: 
        return
    if level>Min_coin: 
        return
    if n==sum:
        Min_coin=min(Min_coin,level)
        return

    for i in range(3):
        sum += coin[i] # 전역변수에 사용한 코인 값 더하기
        DFS(level+1)
        sum -= coin[i] # 리턴 후 전역변수의 값에 더했던 값을 빼서 원상복구!!

DFS(0)  # LEVEL
print(Min_coin)