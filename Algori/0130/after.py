T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input())) # '667767'
    counts = [0] * 10 # 0~9 숫자 이용

    # 숫자의 개수를 세어서 counts 리스트에 저장
    for number in cards: # 요소 반복형태
        counts[number] += 1 # 현재 넘버 위치에

    # print(counts)
    # [0, 0, 0, 0, 0, 0, 3, 3, 0, 0]

    is_babygin = 0
    for idx in range(len(counts)):
        # triplet 확인
        if counts[idx] >= 3: # = 3 은 안됨. 5,5,5,5,6,7
            # 연속 된 트리플랫이 존재하는 경우
            if counts[idx] == 6:
                is_babygin = 2
                break
            # 현재 트리플랫이다
            counts[idx] -= 3 # 트리플으로 사용했기에 갯수 감소
            is_babygin += 1 # 베이비진으로써 만족했기 때문에 후보로서 1 증가

        # run확인
        # 현재위치부터 우측으로 세개씩 확인, 마지막 두개는 우측으로 +2하면 아웃오브레인지나옴
        if idx < len(counts) - 2: # 마지막 2칸은 out of range가 되기 때문
            if counts[idx] and counts[idx+1] and counts[idx+2]:
                counts[idx] -= 1
                counts[idx+1] -= 1
                counts[idx+2] -= 1
                is_babygin += 1

    # 2개의 조건을 모두 만족한 것이 있는지 확인
    if is_babygin == 2:
        print(f'#{tc} "true"')
    else:
        print(f'#{tc} "false"')
    # if is_babygin == 2:
    #     print('베이비진')
    # else:
    #     print('아님')
    # print(f'#{tc} {"true" if is_babygin == 2 else "false"}')'
        

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().strip()))
    # 숫자가 붙어 있는 상태이므로 split은 쓰지 않음
    counts = [0] * 12
    
    for i in arr:
        counts[i] += 1
    i = 0
    is_babygin = 0
    while i < 10:
        if counts[i] >= 3:
            counts[i] -= 3
            is_babygin += 1
            continue 
        # run인지 확인
        if counts[i] >= 1 and counts[i+1] >= 1 and counts[i+2] >= 1:
            counts[i] -= 1
            counts[i + 1] -= 1
            counts[i + 2] -= 1
            is_babygin += 1
            continue
        i += 1
    if is_babygin == 2:
        print(f'#{tc} true')
    else:
        print(f'#{tc} false')