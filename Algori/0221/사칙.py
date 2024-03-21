T = 10
for tc in range(1, T+1):
    N = int(input())
    left = [0] * (N+1) 
    right = [0] * (N+1)
    tree = [0] * (N+1) 
    for i in range(N):
        
        s = input().split()
        if len(s)==4: 
            tree[int(s[0])] = s[1]
            left[int(s[0])] = int(s[2])
            right[int(s[0])] = int(s[3])
        else: 
            tree[int(s[0])] = int(s[1]) 

    def post_order(v):
        if v == 0: # 기저조건
            return
        post_order(left[v]) 
        post_order(right[v])
        
        if tree[v] == '+':
            tree[v] = tree[left[v]] + tree[right[v]]
        elif tree[v] == '-':
            tree[v] = tree[left[v]] - tree[right[v]]
        elif tree[v] == '/':
            tree[v] = tree[left[v]] // tree[right[v]]
        elif tree[v] == '*':
            tree[v] = tree[left[v]] * tree[right[v]]
    post_order(1) # 루트노드 1에 대해서 후위 순회...

    print(f'#{tc} {tree[1]}')