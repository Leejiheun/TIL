T = int(input())

hex_to_bin = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}

for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    N, hex_num = input().split()
    #1 딕셔너리
    for h in hex_num:
        # 0 ~ 15 -> 대응되는 이진법숫자
        # print(h, end=' ')
        print(hex_to_bin[h], end='')
    print()
    #2 int와 formating 사용 - 함수 + 포맷팅
    dec_num = int(hex_num, 16)
    # print(dec_num)
    # print(f'{dec_num:#b}'[2:])  # #b, #o, #x
    # N 16진수의 개수 -> 2진수 N * 4
    bin_num = f'{dec_num:#b}'[2:]
    # 내가 목표로하는 정상적인 길이가 아닐 경우 해당 길로 맞춰주기 위해
    # 0이라는 값을 넣어주기위한 기능(우측맞춤)
    # print(bin_num.rjust(int(N)*4, '0'))
    print(bin_num.zfill(int(N)*4))