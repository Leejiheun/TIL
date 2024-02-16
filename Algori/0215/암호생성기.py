from collections import deque

for i in range(10):
    T = int(input())
    arr = list(map(int, input().split()))

    q = deque()
    for a in arr:
        q.append(a) # enqueue()

    while q[-1] != 0:
        for n in range(1, 6):
            # tmp = q.popleft()-n
            # if tmp < 0:
            #     tmp = 0
            # q.append(tmp)
            q.append(q.popleft() - n)
            # if q[-1] < 0:
            #     q[-1] = 0
            q[-1] = max(0, q[-1])
            if q[-1] == 0:
                break
    print(f'#{T}', *q)

# 은비 언니 풀이
