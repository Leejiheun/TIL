T = int(input())
arr = [list(map(int, input().split())) for _ in range(100)]


total1 = 0
total2 = 0
for i in range(100): # 왼쪽 시작 대각선
    total1 += arr[i][i]

for i in range(100): # 오른쪽 시작 대각선
    total2 += arr[i][100-1-i]

new_list_i = []
for i in range(100):
    new_list_i.append(sum(arr[i]))

new_list_j = []
for j in range(100):
    col_sum = 0
    for i in range(100):
        col_sum += arr[i][j]
    new_list_j.append(col_sum)

result_list = [total1, total2, max(new_list_i), max(new_list_j)]
max_value = max(result_list)
print(f'#{T} {max_value}')

