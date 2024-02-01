T = int(input())

def binary_search(N, k): # N은 전체페이지 # k는 갖고 있는 페이지
    start = 1
    end = N
    times = 0
    while start <= end:
        middle = (start + end) // 2
        if middle == k:
            # times += 1
            return times
        elif middle > k:
            end = middle
        else:
            start = middle
        times += 1
    return times

# 전체 p, 한사람 a, 한사람 b
for tc in range(T):
    p, a, b = list(map(int, input().split()))
    pa = binary_search(p, a)
    pb = binary_search(p, b)
    if pa < pb:
        result = 'A'
    elif pa > pb:
        result = 'B'
    else:
        result = 0
    print(f'#{tc+1} {result}')

# 강사님
# T = int(input())  # 테스트 케이스의 수를 입력받습니다.
#
# def binary_search(start, end, target):
#     cnt = 0  # 이진 탐색을 수행하는 데 필요한 단계 수를 카운트합니다.
#     while start <= end:  # 시작점이 끝점보다 작거나 같을 때까지 반복합니다.
#         middle = (start + end) // 2  # 중간점을 계산합니다.
#         if middle == target:  # 중간점이 타겟과 같으면 탐색을 종료합니다.
#             break
#         if middle < target:  # 중간점이 타겟보다 작으면 시작점을 중간점으로 이동합니다.
#             start = middle
#         else:  # 중간점이 타겟보다 크면 끝점을 중간점으로 이동합니다.
#             end = middle
#         cnt += 1  # 단계 수를 증가시킵니다.
#     return cnt  # 단계 수를 반환합니다.
#
# for tc in range(1, T+1):  # 각 테스트 케이스에 대해
#     P, A, B = map(int, input().split())  # P, A, B를 입력받습니다.
#     a_cnt = binary_search(1, P, A)  # A에 대한 이진 탐색을 수행하고 단계 수를 저장합니다.
#     b_cnt = binary_search(1, P, B)  # B에 대한 이진 탐색을 수행하고 단계 수를 저장합니다.
#     result = 0
#     if a_cnt < b_cnt:  # A의 단계 수가 B의 단계 수보다 작으면 결과는 'A'입니다.
#         result = 'A'
#     if a_cnt > b_cnt:  # A의 단계 수가 B의 단계 수보다 크면 결과는 'B'입니다.
#         result = 'B'
#     print(f'#{tc} {result}')  # 결과를 출력합니다.