# 고지식한 문제
# tc = int(input())
# F = input() # 찾을 문자
# arr = input() # 전체 문자
#
# M = len(F) # 찾을 문자열 길이
# N = len(arr) # 전체 문자열 길이
#
# i = 0
# j = 0
#
# while i < M and j < N:
#     if arr[i] != F[j]:

# 1. 고지식한(브루트포스) 문제로 풀어보기
# text가 원본을 유지하는게 있고, 소거하는 방법이 있음
def bf(pattern, text):
    len_t = len(text)
    len_p = len(pattern)
    i = 0 # 전체 텍스트에서 탐색에 쓸 인덱스
    j = 0 # 패턴 탐색에 쓸 인덱스
    count = 0 # 전체 변수가
    # j = i = 0
    while i < len_t and j < len_p:
        # 현재 탐색하고 있는 문자와 해당 위치와 대응되는 패턴 문자가 다를 때
        if text[i] != pattern[j]: # 탐색 실패
            i = i - j
            j = -1
        i += 1
        j += 1
        # 패턴을 만족시켰을 때
        if j == len_p: # len_p-1까지 탐색 완료
            # 개별 위치 찾을 때 : 인덱스를 리턴 -> i - len_p
            count += 1
            i = i - j + 1
            j = 0
        return count


# # T = 10
# for _ in range(T):
#     tc = input() # 그대로 프린트돼서 굳이 int안해도 됨
#     pattern = input()
#     text = input()
#     result = bf(pattern, text)
#     print(f'#{tc} {result}')

# 2. 파이썬 내장 메서드 사용
# for in range(10):
#     tc = int(input())
#     F = input()
#     arr = input()
#     i = 0
#     cnt = 0
#     while i < len(arr):
#         if F[0] == arr[i]:
#             if F[:] == arr[i:i+len(F)]:
#                 cnt += 1
#                 i += len(F)
#             else:
#                 i += 1
#         else:
#             i += 1
#     print(f'#{tc} {cnt}')