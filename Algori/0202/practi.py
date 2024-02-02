# # 풍선팡2
# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
# T = int(input())
#
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     max_v = 0
#     for i in range(N):
#         for j in range(M):
#             cnt = arr[i][j]
#             for t in range(4):
#                 for l in range(1, arr[i][j]+1):
#                     ti = i + di[t]*l
#                     tj = j + dj[t]*l
#                     if 0 <= ti <= N-1 and 0 <= tj <= M-1:
#                         cnt += arr[ti][tj]
#             if max_v < cnt:
#                 max_v = cnt
#     print(f'#{tc} {max_v}')
#
#
#
# # view
# T = 10
# # 리스트의 0부터 확인
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     result = 0
# # 만약, 인덱스값이 0이 아니라면, -2,-1, 1, 2 값을 비교해줘야함
#     for idx in range(N):
#         if arr[idx] != 0:
#             dj=[-2, -1, 1, 2]
#             max_val = 0
#             for i in range(4):
#                 if max_val < arr[idx-dj[i]]:
#                     max_val = arr[idx-dj[i]]
#             if arr[idx] > max_val:
#                 result += (arr[idx]-max_val)
#
# # 현재인덱스값보다 큰게 있다면~pass, 현재인덱스값이 가장크면 현재인덱스값 - max값


T = int(input()) # 숫자 (int 생략하면 str 상태)
# import math
# def solution1(arr, neighbor):
#     sum_val = sum(arr[0:neighbor])
#     min_val = max_val = sum_val
#     print('min', min_val, 'max', max_val, 'sum', sum_val)
#     for i in range(0, len(arr) - neighbor + 1):
#         sum_val = sum(arr[i:i+neighbor])
#         min_val = min(min_val, sum_val)
#         max_val = max(max_val, sum_val)
#         print('i', i, 'min', min_val, 'max', max_val, 'sum', sum_val)
#     return max_val - min_val

for t in range(T):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    print(f'#{t+1} {solution1(a, M)}')
    sum_val = sum(arr[0:neighbor])
    min_val = max_val = sum_val
    print('min', min_val, 'max', max_val, 'sum', sum_val)
    for i in range(0, len(arr) - neighbor + 1):
        sum_val = sum(arr[i:i + neighbor])
        min_val = min(min_val, sum_val)
        max_val = max(max_val, sum_val)
    print(max_val - min_val)