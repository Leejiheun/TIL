from itertools import combinations

N, M = map(int, input().split())
arr = list(map(int, input().split()))

lst = list(combinations(arr, 3))

n_lst = []

for i in range(len(lst)):
    n_lst.append(sum(lst[i]))

n_lst.sort()
check = []
for j in range(len(n_lst)):
    if M > n_lst[j]:continue
    if M < n_lst[j]:
        print(n_lst[j-1])
        break
    if M == n_lst[j]:
        print(n_lst[j])
        break