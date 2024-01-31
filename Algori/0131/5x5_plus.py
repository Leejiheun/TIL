# 5*5 2차 배열에 25개의 숫자를 저장하고,
# 대각선 원소의 합을 구하시오
T = int(input())
arr = [list(map(int, input().split())) for _ in range(T)]
total = 0
for i in range(T):
    total += arr[i][i]
    total += arr[i][T-1-i]
if N%2:
    total