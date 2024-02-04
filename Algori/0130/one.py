T = int(input())
for t in range(T):
    N = int(input())
    seq = input().strip().split('0')  # 0을 기준으로 시퀀스를 분할합니다. 이렇게 하면 '1'로만 이루어진 부분 시퀀스들을 얻을 수 있습니다.
    result = max([len(el) for el in seq])  # 각 부분 시퀀스의 길이 중 최대값을 찾습니다. 이 값이 연속된 '1'의 최대 개수가 됩니다.
    print(f'#{t+1} {result}')  # 결과를 출력합니다.

T = int(input())
 
for tc in range(1,T+1):
    N = int(input())
    arr = input().strip().split('0')

    new_list = []
    for i in arr:
        new_list.append(len(i))
        result = max(new_list)
    print(f'#{tc} {result}')

T = int(input())
 
for tc in range(1,T+1):
    N = int(input())
    arr = input().strip().split('0')
    new_list=[]
    for i in arr:
        new_list.append(len(i))
        
    print(f'#{tc} {max(new_list)}')