# 테스트 케이스 T를 받는다(input)
T = int(input()) # 테스트 케이스의 수 타입으로 받을 수 있다.
# print(T, type(T))
for t in range(T): # T번 반복해서 테스트 케이스별 입력 받기
    N = int(input()) # N개의 입력
    # a = input().split() # string은 리스트
    # a = map(int, input().split())  # 각각의 요소 string을 int로 변환
    a = list(map(int, input().split())) # 맵은 자료구조 변환 전까지 그냥 맵
    # print(a)
    max_val = max(a)
    min_val = min(a)
    print(f'#{t+1} {max_val - min_val}')