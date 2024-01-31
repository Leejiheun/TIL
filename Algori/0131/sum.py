T = int(input())
arr = [list(map(int, input().split())) for _ in range(100)]


total1 = 0
total2 = 0
for i in range(100): # 왼쪽 시작 대각선
    total1 += arr[i][i]
# for i in range(100): # 오른쪽 시작 대각선
#     total2 += arr[i][100-1-i]

new_list_i = []
for i in range(100):
    new_list_i.append(sum(arr[i]))

new_list_j = []
for j in range(100):
    new_list_j.append(sum(arr[:][j]))

result_list = []
result_list.append(total1)
# result_list.append(total2)
result_list.append(new_list_i)
result_list.append(new_list_j)
x = max(result_list[1])
print(f'#{T} {x}')

