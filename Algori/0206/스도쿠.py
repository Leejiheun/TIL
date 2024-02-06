T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    new_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in range(9):
        temp1 = []
        for j in range(9):
            if arr[i][j] not in temp1:
                temp1.append(arr[i][j])
        if len(temp1) != 9:
            print('0')

    for j in range(9):
        for i in range(9):
            temp2 = []
            if arr[i][j] not in temp2:
                temp2.append(arr[i][j])
        if len(temp2) != 9:
            print('0')

    for x in range(0, 9, 3):
        for x_x in range(x, x+3):
            for y in range(0, 9, 3):
                for y_y in range(y, y+3):
                    temp3 = []
                    if arr[x_x][y_y] not in temp3:
                        temp3.append(arr[x_x][y_y])
                if len(temp3) != 9:
                    print('0')
    print('1')