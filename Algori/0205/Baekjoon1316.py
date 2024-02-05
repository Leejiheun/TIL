T = int(input())
for tc in range(1, T+1):
    arr = list(map(str, input().split()))
    cnt = 0

    for i in range(len(arr)):
        for k in range(1, len(arr)):
            if arr[i] != arr[k]:
                pass

T = int(input())
cnt = 0
for _ in range(T):
    arr = list(input())
    i = 0
    check = True
    for i in range(len(arr) - 1):
        j = i + 1
        if arr[j] == arr[i]:
            while j < len(arr) and arr[j] == arr[i]:
                j += 1
        while j < len(arr):
            if arr[j] == arr[i]:
                check = False
            j += 1
    if check == True:
        cnt += 1
    else:
        pass
print(cnt)