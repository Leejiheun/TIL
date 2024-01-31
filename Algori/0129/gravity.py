N = int(input()) # 상자가 쌓여있는 가로 길이
arr = list(map(int, input().split()))

max_v = 0 # 가장 큰 낙차

for i in range(N-1): # i는 낙차를 구할 위치
    cnt = 0 # 오른쪽에 있는 더 낮은 높이의 개수
    for j in range(i+1, N):
        if arr[i]>arr[j]:
            cnt += 1
    if max_v < cnt:
        max_v = cnt

print(f'#{i} {max_v}')