T = int(input())
n_n = 0
result = 0
for tc in range(T):
    num = [list(map(int, input().split())) for _ in range(T)]
    num.sort()

    i = 0 # 높이가 최대인 번호(인덱스) 구하기
    for n in num:
        if n[1] > n_n:
            n_n = n[1]
            idx = i
        i += 1
    h = num[0][1] # 초기 높이 값은 젤 앞에 높이로 설정

    for i in range(idx):
        if h < num[i+1][1]:
            area = h * (num[i+1][0]-num[i][0])
            result += area
        else:
            area = h * (num[idx][0]-num[i][0])
            result += area
    
    h = num[-1][1]

    # for i in range(idx):
    #     if h < num[-1-i][1]:
    #         area = h * (num[i+1][0]-num[i][0])
    #         result += area
    #     else:
    #         area = h * (num[idx][0]-num[-1-i][0])
    #         result += area
    # print(result)