T = int(input())
n_n = 0 # 최대값 높이
result = 0

#
for tc in range(T):
    num = [list(map(int, input().split())) for _ in range(T)]
    num.sort()
    print(num)
    i = 0  # 높이가 최대인 번호(인덱스) 구하기
    for n in num:
        if n[1] > n_n:
            n_n = n[1]
            idx = i
        i += 1
    # print(idx) # idx는 최댓값인덱스 3, i는 7

    h = num[0][1]  # 초기 높이 값은 젤 앞에 높이로 설정
    for k in range(idx): # 0 1 2
        if h < num[k + 1][1]:
            area = h * (num[k + 1][0] - num[k][0])
            result += area
        else:
            area = h * (num[idx][0] - num[k][0])
            result += area
    print(result)

    h = num[-1][1]
    for k in range(1, len(num) - idx):  # 1 2 3
        if h < num[-1 - k][1]:
            area = h * (num[-1 - k][0] - num[-1 - (k + 1)][0])
            result += area
        else:
            area = h * (num[-1 - k][0] - num[idx][0])
            result += area
    print(result)