import sys
sys.stdin = open("sample_input (1).txt")

T = int(input())
for tc in range(1, T+1):
    n, hexnum = input().split()
    int_num = int(hexnum, 16)
    bin_res = f'{int_num:#b}'[2:].zfill(int(n)*4)
    print(f'#{tc}', bin_res)