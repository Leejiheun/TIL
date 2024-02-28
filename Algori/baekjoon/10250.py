T = int(input())

for tc in range(1, T+1):
    H, W, N = map(int, input().split()) #  각각 호텔의 층 수, 각 층의 방 수, 몇 번째 손님
    arr = [[0]*W for _ in range(H)]
    cnt = 0
    for j in range(W):
        for i in range(H-1, -1, -1):
            cnt += 1
            if cnt == N:
                if 0 < j+1 < 10:
                    a = H-i
                    a = str(a)
                    b = j+1
                    b = str(b)
                    print(a, '0', b, sep='')
                else:
                    a = H-i
                    a = str(a)
                    b = j+1
                    b = str(b)
                    print(a,b, sep='')