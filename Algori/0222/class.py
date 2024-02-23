# N = int(input())
# arr = [[0] * 7 for _ in range(2)]
# t1 = N
# for i in range(N-1):
#     arr[0][i] = t1
#     t1 += 1
#
# for i in range(N+1, N-3, -1):
#     arr[1][i] = t1
#     t1 -= 1
# print(arr[0])
# print(arr[1])


# # 시험 코드르 제출 할 때는 주석 처리 하기
# import sys
# sys.stdin = open('input.txt', 'r')\
#
# n = int(input())
# print(n)

import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

a, b = map(int, input().split())

print(a+b)
print(a*b)