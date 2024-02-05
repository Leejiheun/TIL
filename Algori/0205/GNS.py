# T = int(input())
# for _ in range(T):
#     tc, P = map(str, input().split())
#
#     N = int(P)
#     str1 = list(map(str, input().split()))
#     lst = []
#     idx_dict = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}
#     numbers = "ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"
#     new_lst = list(numbers)
#
#     for K in range(10):
#         char = new_lst[K]
#         a = str1.count(char)
#         pre_result = char + " "
#         lst.append(pre_result * a)
#
#     print(tc)
#     print(*lst)



T = int(input())
for _ in range(T):
    N, M = input().split()
    arr = list(map(str, input().split()))
    num_list = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    M = int(M)
    print(N)
    for i in range(10):
        for tc in range(M):
            if num_list.index(arr[tc]) == i:
                print(arr[tc], end=' ')
        print()