import sys
input = sys.stdin.readline

T = int(input())
lst = [0] * 10001

arr = []

for tc in range(T):
    x = int(input())
    lst[x] += 1

for i in range(len(lst)):
    while lst[i] > 0:
        print(i)
        lst[i] -= 1

import sys
input = sys.stdin.readline

n = int(input())
arr = [0] * (10000+1) # 입력값이 10000까지니깐

# 각 입력값에 해당하는 인덱스 값 증가
for _ in range(n):
    arr[int(input())] += 1

# arr 에 기록된 정보 확인
for i in range(len(arr)):
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i)