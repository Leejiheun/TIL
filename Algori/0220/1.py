T = 10

def in_order(arr, i):
    if arr[i]:
        print(arr[i], end = '')
        in_order(arr, child_info[i][0])
        in_order(arr, child_info[i][1])

for tc in range(T):
    N = int(input())
    node = [0] * (N+1)
    child_info = [[0,0] for _ in range(N+1)]

    for n in range(N):
        i, nod, *ch = input().split()
        i = int(i)
        node[i] = nod
        ch = list(map(int, ch))
        if len(ch) == 2:
            child_info[i] = ch
        if len(ch) == 1:
            child_info[i][0] = ch[0]

    print(f'#{tc+1}', end= ' ')
    in_order(node, 1)
    print()