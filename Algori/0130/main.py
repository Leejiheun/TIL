N = 6
K = 9
data = [7, 2, 4, 5, 2, 3]
counts = [0] * (k+1)
temp = [0]*N
for x in data:
    counts[x] += 1
# counts 누적합 구하기
for i in range(1, k+1):
    counts[i] = couts[i-1] + counts[i]
for i in range(N-1, -1, -1):
    counts[data[i]] -= 1
    temp[counts[data[i]]] = data[i]
print(*temp)