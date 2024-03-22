import sys
sys.stdin = open("sample_input (1).txt")

T = int(input())

for tc in range(1, T+1):
    n, hexnum = input().split()
    int_num = int(hexnum, 16)
    bin_num = bin(int_num)
    print(f'#{tc}', str(bin_num)[2:].zfill(int(n)*4))