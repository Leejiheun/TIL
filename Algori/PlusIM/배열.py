# 델타연습

arr = [ [3, 5, 4, 5, 6],
        [1, 1, 2, 7, 8],
        [1, 2, 9, 1, 2],
        [3, 5, 4, 5, 6],
        [1, 1, 2, 7, 8]]

# 위 아래 좌 우로 3칸까지 떨어진 곳들의 합을 구하기
# 2 2 입력시  18 가 출력이 됩니다. # (9+9=18)
# 0 0 입력시  19 가 출력이 됩니다. # (1+5+1+4+3+5)

y, x = map(int, input().split())
directy = [1,-1,0,0] # 위 아래 좌 우
directx = [0,0,-1,1]

Sum = 0

for i in range(4):
    for j in range(1, 4):
        dy = y + directy[i] * j
        dx = x + directx[i] * j
        if 0 <= dy < x and 0 <= dx < x:
            sum += arr[dy][dx]
print(Sum)
