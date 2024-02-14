T = int(input())

def rsp(idx1, idx2):
    # idx1 < idx2 : 비겼을 때 인덱스가 작은 쪽이 이긴다
    card1 = cards[idx1]
    card2 = cards[idx2]
    # 1 : 가위, 2 : 바위, 3 : 보
    if card1 == '1' and card2 == '2': # 가-바
        return idx2  # 큰 인덱스가 이길 수 있는 3가지 조건
    if card1 == '2' and card2 == '3': # 바-보
        return idx2
    if card1 == '3' and card2 == '1': # 보-가
        return idx2
    return idx1  # 비겨도 얘가 이김, 이겨도 얘가 이김.

def divide(start, end):
    if start == end:
        return start # 한 점으로 수렴한 것을.
    # i ~ (i+j) // 2 | (i+j) // 2 + 1 ~ j
    mid = (start+end) // 2
    g1 = divide(start, mid)
    g2 = divide(mid+1, end)
    return rsp(g1, g2)



for tc in range(1, T+1):
    _ = input()
    cards = input().split()  #  0 ~ N-1
    # cards를 함수에서 직접 호출해도 문제가 없죠
    print(f'#{tc}', end=' ')
    answer = divide(0, len(cards) - 1)  #
    # 1 ~ N. -> start, end. divide 0 ~ N-1.
    print(answer + 1)  # 1씩 시작하는 숫자로 변경

