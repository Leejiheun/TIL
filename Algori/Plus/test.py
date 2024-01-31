#import sys
#sys.stdin = open("input.txt", "r")

T = 10  # 테스트 케이스
for tc in range(1, T+1): # 1에서 10까지
    N = int(input())    # 빌딩의 개수

# N개의 건물 높이가 주어짐
building_list = list(map(int, input().split()))

# 확보된 조망권을 저장할 수 있는 변수
result = 0

for idx in range(N): # 첫번째 빌딩부터
    if building_list[idx] != 0:  # 빌딩 높이가 0이 아닌 것만 (0이라는 의미는 빌딩이 없다는 의미)
        # 빌딩이 존재한다면
        # 좌, 우 2칸씩 확인을 해야 함
        nxt_index = [-2, -1, 1, 2]  # 좌측, 우측 두 개씩 확인하기 위한 index 를 준비
        max_height = 0              # 가장 높은 빌딩의 높이를 저장하기 위함
        # 총 4개의 빌딩을 확인해야 하니까
        for i in range(4): # 0,1,2,3
            # 최대 높은 건물을 우선 찾자!!
            if max_height < building_list[idx + nxt_index[i]]: # 0 1 3 4
                max_height = building_list[idx + nxt_index[i]]  # 최대 높이를 갱신

        # 현재 높이보다 좌우 건물이 더 낮아야 함!
        if building_list[idx] > max_height:
            result += building_list[idx] - max_height
    # else: # 빌딩 높이가 0인 것은 확인할 필요가 없음
    #     pass

print(f'#{tc} {result}')
