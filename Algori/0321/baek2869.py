A, B, V = map(int, input().split())
cnt = 0
h = A - B

while h <= V:

    h = h + (A-B)
    cnt += 1

print(cnt-1)