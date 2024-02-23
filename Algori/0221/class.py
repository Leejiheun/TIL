# 최대 힙 구현하기
def enq(n):
    global last
    last += 1   # 마지막 노드 추가( 완전이진트리 유지 )
    h[last] = n # 마지막 노드에 데이터 삽입
    c = last    # 부모 > 자식 비교를 위해
    p = c//2    # 부모번호 계산
    # 힙에 대한 삽입 연산
    while p >= 1 and h[p] < h[c]: # 부모가 있는데, 더 작으면 둘이 교환해
        h[p], h[c] = h[c], h[p] # 교환
        c = p
        p = c//2

# 삭제
def deq():
    global last
    tmp = h[1] # 루트의 키값 보관 (임시 보관)
    h[1] = h[last] # last를 루트노드로
    last -= 1
    p = 1   # 새로 옮긴 루트값
    c = p* 2 # 자식 비교
    while c <= last: # 자식이 하나라도 있으면
        if c+1 <= last and h[c] < h[c+1]: # 오른쪽 자식이 있고, 왼쪽 자식보다 오른쪽 자식이 더 크면
            c += 1 # 오른쪽 자식과 비교
        if h[p] < h[c]: # 힙의 부모와 힙의 자식 비교
            h[p], h[c] = h[c], h[p]
            p = c
            c = p*2
        else:
            break
    return tmp


N = 10          # 필요한 노드 수
h = [0] * (N+1) # 최대힙
last = 0 # 힙의 마지막 노드 번호

enq(2)
enq(5)
enq(3)
enq(6)
enq(4)

while(last>0):
    print(deq())