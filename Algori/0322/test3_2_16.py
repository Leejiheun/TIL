import sys
sys.stdin = open("sample_input (1).txt")

T = int(input())
for tc in range(1, T+1):
    n, hexnum = input().split()
    bin_num = int(hexnum, 16)
    bin_result = f'{bin_num:#b}'[2:].zfill(int(n)*4) # bin_result 는 2진수
    int_num = int(bin_result, 2) # 2진수를 10진 수로 바꿔주기
    print(f'#{tc}', hex(int_num)[2:].upper())