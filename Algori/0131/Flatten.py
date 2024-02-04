# 총 10개의 테스트 케이스가 주어지며(제약되어 있음)
T = 10  # 테스트 케이스의 수를 설정합니다.

def counting(data): # heights = data
    k = max(data)  # 입력 데이터의 최대값을 찾습니다.
    length = len(data)  # 입력 데이터의 길이를 계산합니다.
    counts = [0] * (k+1)  # 각 숫자의 개수를 저장할 리스트를 초기화합니다.
    # 인덱스가 0부터 시작하기 때문에 마지막 인덱스를 K라고 하기 위해서!
    for i in range(length):  # 입력 데이터의 각 요소에 대해
        counts[data[i]] += 1  # 해당 요소의 개수를 세어 저장합니다.
    return counts  # 개수를 센 결과를 반환합니다.

for tc in range(T):  # 각 테스트 케이스에 대해/직접 10을 넣어도 됨
    dump = int(input())  # 덤프 횟수를 입력받습니다.
    heights = list(map(int, input().split()))  # 각 상자의 높이를 입력받습니다. # 땅의 높이
    counted = counting(heights)  # counting 함수를 호출하여 각 높이의 상자 개수를 계산합니다.
    # print(counted) : 0은 0개 1은 *개, ...
    start = 1  # 현재 가장 작은 건물의 높이 # 가장 낮은 높이를 저장할 변수를 초기화합니다.
    end = len(counted) - 1 # 현재 가장 큰 건물의 높이 # 가장 높은 높이를 저장할 변수를 초기화합니다.
    # 높이별 현재 현황을 나타낸 counted
    while dump > 0:  # 덤프 횟수만큼 반복합니다.
        # 시작지점이나 종료지점 비어있으면 가운데 방향으로 이동
        # 한번 덤핑 하면,,
        # 가장 작은 경우 -> -1. 그 다음 숫자가 +1 / 1이 줄어들면 2가 하나 올라감
        # 가장 큰 경우 -> -1. 그 이전 숫자가 +1
        if counted[start] == 0:  # 가장 낮은 높이의 상자가 없다면 # if not counted[start]:
            start += 1  # 가장 낮은 높이를 1 증가시킵니다.
            continue # 너 지금 잘 못 된 스타트 점이야, 다음으로 움직여
        if not counted[end]:  # 가장 높은 높이의 상자가 없다면
            end -= 1  # 가장 높은 높이를 1 감소시킵니다.
            continue
        counted[start] -= 1  # 가장 낮은 높이의 상자 개수를 1 감소시킵니다.
        counted[start+1] += 1  # 그 다음 높이의 상자 개수를 1 증가시킵니다.
        counted[end] -= 1  # 가장 높은 높이의 상자 개수를 1 감소시킵니다.
        counted[end-1] += 1  # 그 다음 낮은 높이의 상자 개수를 1 증가시킵니다.
        dump -= 1  # 덤프 횟수를 1 감소시킵니다. # 평탄화작업
    # 한번 더 중앙으로 움직이는 것 검사
    # 원칙적으로는 이것만의 0을 피하기 위한 추가 검사
    if not counted[start]:  # 가장 낮은 높이의 상자가 없다면
        start += 1  # 가장 낮은 높이를 1 증가시킵니다.
    if not counted[end]:  # 가장 높은 높이의 상자가 없다면
        end -= 1  # 가장 높은 높이를 1 감소시킵니다.
    print(f'#{tc+1} {end - start}')  # 가장 높은 높이와 가장 낮은 높이의 차이를 출력합니다.


for test in range(10):
    dump = int(input())
    lst = list(map(int, input().split()))
    for d in range(dump):
        max_ = max(lst)
        min_ = min(lst)
        lst[lst.index(max_)] = max_-1
        lst[lst.index(min_)] = min_+1
 
    print(f"#{test+1} {max(lst)-min(lst)}")

T = 10
for x in range(T):
    total = int(input())
    testcase = list(map(int, input().strip().split(" ")))
    for i in range(total):
        max_box = max(testcase)
        min_box = min(testcase)
        max_index = testcase.index(max(testcase))
        min_index = testcase.index(min(testcase))
        max_box -= 1
        min_box += 1
        testcase[max_index] = max_box
        testcase[min_index] = min_box
    max_box = max(testcase)
    min_box = min(testcase)
    print(f'#{x+1} {max_box - min_box}')


T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(N):
        max_num = max(arr)
        min_num = min(arr)
        arr[arr.index(max_num)] = max_num - 1
        arr[arr.index(min_num)] = min_num - 1
        
    print(f'#{tc} {max(arr)-min(arr)}')
