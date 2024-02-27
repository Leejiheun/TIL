T = int(input())
new_list = []

for x in range(1, T+1):
    x = str(x)
    cnt = 0
    for i in x:
        if i == 3 or i == 6 or i == 9:
            cnt += 1
        if cnt > 0:
            new_list.append('-' * cnt)
        else:
            new_list.append(x)
        print(*new_list)