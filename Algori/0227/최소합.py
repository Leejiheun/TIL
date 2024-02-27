T = int(input())

def dfs(i, j, cum_sum):
    
    cum_sum += matrix[i][j]
    
    if i == j == (N-1):
        global min_val
        min_val = min(min_val, cum_sum)
    
    if cum_sum >= min_val:
        return
    
    d = [(0, 1), (1, 0)]
    for di, dj in d:
        ni = i + di
        nj = j + dj
     
        if not 0 <= ni < N:
            continue
        if not 0 <= nj < N:
            continue
       
        if visited[ni][nj]:
            continue
        
        visited[ni][nj] = 1
        dfs(ni, nj, cum_sum)
     
        visited[ni][nj] = 0

for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    N = int(input())
    matrix = [list(map(int, input().split()))
              for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    min_val = 10 * (N * 2 - 1)
    dfs(0, 0, 0)
    print(min_val)