import math

T = int(input())  # 테스트 케이스의 수를 입력 받음

for tc in range(1, T+1):  # 각 테스트 케이스에 대해
    print(f'#{tc}', end=' ')  # 테스트 케이스 번호를 출력
    N = float(input())  # 변환할 실수를 입력 받음
    bin_num = []  # 변환된 2진수를 저장할 리스트 # bin_num =''도 괜찮

    for i in range(12):  # 최대 12자리까지 확인
        if N >= 2 ** (-i-1):  # 만약 현재 자리의 값이 실수보다 작거나 같다면
            bin_num.append('1')  # 2진수에 '1'을 추가
            N -= 2 ** (-i-1)  # 실수에서 현재 자리의 값을 뺌
        else:
            bin_num.append('0')  # 그렇지 않다면 2진수에 '0'을 추가
        if math.isclose(0, N):  # 만약 실수가 0에 가깝다면 (즉, 모든 자리를 확인했다면)
            print(''.join(bin_num))  # 2진수를 출력하고 루프를 종료
            break

    else:  # 12자리를 모두 확인한 후에도 실수가 0이 아니라면 (즉, 2진수로 정확히 표현할 수 없다면)
        print('overflow')  # 'overflow'를 출력

# +
import math

T = int(input())

for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    # N = int(input())
    N = float(input())
    print(N)
    # 소수점1~12자리.
    bin_num = ''
    for i in range(1, 13):
        if N >= 2 ** -i:
            # 분수를 빼줄 수있다
            bin_num += '1'  # 현재 위치를 체크.
            # 문자열로 변환해서 해당 이진수 소수점 자리를 연결
            N -= 2 ** -i
        else: # 새로운 값을 빼주려는데 0보다 작아진 것.
            bin_num += '0'  # 빼줄 수 는 빈자리라서...
        # if math.isclose(0, N):
        if N == 0:
            print(bin_num)
            break
    else:
        print('overflow')