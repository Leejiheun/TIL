# for tc in range(1, int(input())+1):
#     N = int(input())
#     TC = list(map(int, input().split()))
#     max_value = 0

#     for i in range(N):
#         cnt = 0
#         for j in range(i+1, N):
#             if TC[i] > TC[j]:
#                 cnt += 1

#         if cnt > max_value:
#             max_value = cnt

#     print(f'#{tc} {max_value}')

T = int(input())
for x in range(T):
    n = int(input())
    testcase = list(map(int, input().split()))
    count = []
    for i in range(n):
        fall = 0
        for j in range(i + 1, n):
            if testcase[i] > testcase[j]:
                fall += 1
        count.append(fall)
    fall_max = max(count)
    print(f"#{x+1} {fall_max}")

T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    max_val = 0
    for i in range(N):
        fall = 0
        for j in range(i+1, N):
            if arr[i] > arr[j]:
                fall += 1
        if max_val < fall:
            max_val = fall
print(f'#{tc+1} {max_val}')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    testcase = list(map(int, input().split()))
    max_list = []
    for i in range(N):
        fall = 0
        for x in range(i+1, N):
            if testcase[i] > testcase[x]:
                fall += 1
        max_list.append(fall)
    max_num = max(max_list)
    print(f'#{tc} {max_num}')