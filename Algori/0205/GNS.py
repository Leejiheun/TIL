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
    # print(N)
    for i in range(10):
        for tc in range(M):
            if num_list.index(arr[tc]) == i:
                print(arr[tc], end=' ')
        print()


# 제갈덕님 풀이
# 1
import sys
sys.stdin = open("input.txt", "r")

code_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]


# "TWO"를 입력하면 2를 반환하고 싶다.
def decode(n):
    return code_list.index(n)


# 2를 입력하면 "TWO"를 반환하고 싶다.
def encode(n):
    return code_list[n]


T = int(input())

for testcase in range(1, T + 1):
    t, N = input().split()
    # n = int(N)
    lst = list(map(decode, input().split()))
    lst.sort()
    result = list(map(encode, lst))
    print(t, *result)

#2
import sys
sys.stdin = open("input.txt", "r")

# 2. Not using function

T = int(input())
code_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for testcase in range(1, T + 1):
    _ = input() # 앞에서 봤듯이 쓸모없는 input이었다.
    lst = list(input().split())

    lst_decoded = []
    for number in lst:
        lst_decoded.append(
            code_list.index(number)
        ) # .index()로 append된 원소들은 모두 int이다. 따라서 lst_decoded는 int로만 이루어진 list

    # int들로 이루어진 list를 sort
    lst_decoded.sort()

    # 이름은 result지만, lst_encoded라고 봐도 된다.
    result = []
    for i in lst_decoded:
        result.append(code_list[i])

    # print(f'{testcase}, {*result}') <= 얘는 왜인지 모르겠는데 안됨
    print(f'#{testcase}', *result)


# 연습
T = int(input())
N, M = map(int, input().split())
arr = list(map(int, input().split()))
new_list = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

for tc in range(1, T+1):
    M = int(M)
    for i in range(M):
        if new_list.index(arr[i]) == i:
            