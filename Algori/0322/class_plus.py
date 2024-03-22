# import sys
# sys.stdin = open("sample_input (1).txt")

# T = int(input())  # 테스트 케이스의 수를 입력 받음

# for tc in range(1, T+1):  # 각 테스트 케이스에 대해
#     print(f'#{tc}', end=' ')  # 테스트 케이스 번호를 출력
#     N, hex_num = input().split()  # 16진수의 길이(N)와 16진수(hex_num)를 입력 받음
#     # 만약 int가 금지라면 dictionary로 for문 처리 + 16 ** (len(N) - 1 - i)로 순회
#     dec = int(hex_num, 16)  # 16진수를 10진수로 변환
#     tmp = f'{dec:#b}'[2:]  # 10진수를 2진수로 변환하고, 앞의 '0b'를 제거
#     # print('0' + tmp if len(tmp) % 2 else tmp)  # 만약 2진수의 길이가 홀수라면 앞에 '0'을 추가하여 출력 (현재 주석 처리됨)
#     print(f'{dec:#b}'[2:].zfill(int(N) * 4))  # 2진수를 출력하되, 필요한 경우 앞에 '0'을 추가하여 길이를 4N으로 맞춤

# 5185
import sys
sys.stdin = open("sample_input (1).txt")

T = int(input())
for tc in range(1, T+1):
    n, hexnum = input().split()

    # 1. 함수 사용
    # print(int(hexnum, 16)) # 16진접의 숫자를 받아서 헥사로 받겠다
    int_num = int(hexnum, 16)
    print(int_num, 16)
    bin_num = bin(int_num) # 이진법으로 바꿔줌 ob는 bin라는걸
    #------------------ 포맷팅 사용 방법
    print(bin_num)
    print(str(bin_num)[2:])
    print(str(bin_num)[2:].zfill(int(n)*4)) # zfill 빈것만큼 0을 앞에 붙여줌, (int(n)*4)) 16진수를 2진수를 바꾸면 자릿수가 4배가 되어야함. 반대의 경우 신경X 16진수를 2진수로 바꾸면 생각해줘야함
    bin_result = f'{int_num:#b}'[2:].zfill(int(n)*4)
    print(f'{int_num:#x}'[2:])
    print('--------------')
    print(f'{int_num:#b}')
    # 16진법을 2진법으로 바꿀 수 있다.
    # 1-3 ) 2진법 -> 16진법
    print('int(bin_result,2)', int(bin_result, 2))
    int_num2 = int(bin_result, 2)
    print(hex(int_num2))
    print(hex(int_num2)[2:].upper())

#     # 16진법을 2진법으로 바꾸는 
#     hex_to_bin = {
#         '0': '0000',
#         '1': '0001',
#         '2': '0010',
#         '3': '0011',
#         '4': '0100',
#         '5': '0101',
#         '6': '0110',
#         '7': '0111',
#         '8': '1000',
#         '9': '1001',
#         'A': '1010',
#         'B': '1011',
#         'C': '1100',
#         'D': '1101',
#         'E': '1110',
#         'F': '1111',
#     }
#     bin_to_hex = {
#         '0000':'0',
#         '0001':'1',
#         '0010':'2',
#         '0011':'3',
#         '0100':'4',
#         '0101':'5',
#         '0110':'6',
#         '0111':'7',
#         '1000':'8',
#         '1001':'9',
#         '1010':'A',
#         '1011':'B',
#         '1100':'C',
#         '1101':'D',
#         '1110':'E',
#         '1111':'F',
#     }
#     bin_result2 = ''
#     for d in hexnum:
#         print(d, hex_to_bin[d])
#         bin_result2 += hex_to_bin[d]
#     print(bin_result2)
#     hex_result2 = ''
#     for i in range(0, len(bin_result2), 4):
#         print(i, i+4, bin_result2[i:i+4])
#         print(bin_to_hex[bin_result2[i:i+4]])
#         hex_result2 += bin_to_hex[bin_result2[i:i+4]]
#     print(hex_result2)

# # 2진법 -> 16진법 바꾸는거 까지 봐야함, 0 있는지 없는지.
    
# # 2진수랑 16진수랑 섞여서 나올 경우 if문을 사용해서 길이를 나눠서 생각해줌
    