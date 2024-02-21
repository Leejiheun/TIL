# 2628
row, col = map(int ,input().split())
N = int(input())
row_list = [0]
col_list = [0]

for tc in range(N):
    a, b = map(int, input().split())
    if a == 0:
        col_list.append(b)
    else:
        row_list.append(b)
    row_list.append(row)
    col_list.append(col)
    row_list.sort()
    col_list.sort()

area = []
for i in range(len(row_list)-1):
    for j in range(len(col_list)-1):
        x = (col_list[j+1]-col_list[j]) * (row_list[i+1]-row_list[i])
        area.append(x)
print(max(area))