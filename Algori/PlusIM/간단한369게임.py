# 1926 간단한 369게임

N = int(input())
new_list = []
for i in range(1,N+1):
    word = str(i) # 문자열로 바꾸기
    cnt = 0
    # 문자열 길이만큼 탐색해서 3,6,9 몇개인지 찾기

    for i in word:
        if i =='3' or i =='6' or i =='9':
            cnt += 1
        # if i in "369":
        #     cnt += 1
    
    if cnt: # 3또는 6 또는 9가 존재한다면
        new_list.append('-'*cnt)
    else:
        new_list.append(word)
    
print(*new_list)
