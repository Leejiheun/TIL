# 240131_2차원 배열_수업
'''
3
123
456
789
'''
N = int(input())
arr = [list(map(int,input().split()))]
print(arr)
# arr2 = [0]*N
# arr2 = [[0]*N for _ in range(N)]
# arr3 = [[0]*N]*N # 안돼!!
# arr2 : 2차원 배열
# --------------------------
# 배열 순회
'''
n x m 배열의 n*m 개의 모든 원소를 빠짐없이 조사하는 방법
'''
# i 행의 좌표
# j 열의 좌표
for i in range(n):
    fot j in range(m):
    f(array[i])[j] # 행 우선 순회
for i in range(n):
    fot j in range(m):
    f(array[j][i]) # 열 우선 순회

for i in range(n):
    for j in range(m):
        f(array[i][j]+ (m-1-2*j)* (i%2)) # 지그재그 순회
       
for i : 0 -> N-1
    if i % 2 == 0: # 짝수행
        for j : 0 -> N-1
            arr[i][j]
    else:
        for j : M-1 0-> 0
            arr[i][j]


# 2차원 배열 안에서 델타
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
i = 3
j = 4
for k in range(4): # 0 1 2 3
    ni = i + di[k]
    nj = j + dj[k]
    print(ni,nj)
'''
3 5
4 4
3 3
2 4
'''
# -----------
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N = 5
for i in range(N):
    for j in range(N):
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            print((ni,nj), end = ' ')
        print()
'''
# 마이너스..?
(0, 1) (1, 0) (0, -1) (-1, 0) 
(0, 2) (1, 1) (0, 0) (-1, 1) 
(0, 3) (1, 2) (0, 1) (-1, 2)
(0, 4) (1, 3) (0, 2) (-1, 3)
(0, 5) (1, 4) (0, 3) (-1, 4)
(1, 1) (2, 0) (1, -1) (0, 0)
(1, 2) (2, 1) (1, 0) (0, 1)
(1, 3) (2, 2) (1, 1) (0, 2)
(1, 4) (2, 3) (1, 2) (0, 3)
(1, 5) (2, 4) (1, 3) (0, 4)
(2, 1) (3, 0) (2, -1) (1, 0)
(2, 2) (3, 1) (2, 0) (1, 1)
(2, 3) (3, 2) (2, 1) (1, 2)
(2, 4) (3, 3) (2, 2) (1, 3)
(2, 5) (3, 4) (2, 3) (1, 4)
(3, 1) (4, 0) (3, -1) (2, 0)
(3, 2) (4, 1) (3, 0) (2, 1)
(3, 3) (4, 2) (3, 1) (2, 2)
(3, 4) (4, 3) (3, 2) (2, 3)
(3, 5) (4, 4) (3, 3) (2, 4)
(4, 1) (5, 0) (4, -1) (3, 0)
(4, 2) (5, 1) (4, 0) (3, 1)
(4, 3) (5, 2) (4, 1) (3, 2)
(4, 4) (5, 3) (4, 2) (3, 3)
(4, 5) (5, 4) (4, 3) (3, 4)
'''

# delta1
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N = 5
arr = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0<=nj<N:
                print(arr[ni][nj], end = ' ')
            print()
# --------------------
# subset
N = 3
arr = [1,2,3]

for i in range(1<<N): # 2의 N제곱
    for j in range(N):
        if i&(1<<j):
            print(arr[j],end=' ')
    print()
'''
1
2
12
3
13
23
123
'''

# --------
'''
10
-7 -5 2 3 8 -2 4 6 9
'''
def f(arr, N):
    for i in range(1, 1 << N):
        s = 0
        for j in range(N):
            if i & (1 << j):
                s += arr[j]
                #print(arr[j], end=' ')
        #print(s)
        if s == 0:
            return True
    return False

N = int(input())
arr = list(map(int, input().split()))
print(f(arr, N))