import sys
sys.stdin = open("sample_input (1).txt")

T = int(input())
for tc in range(1, T+1):
    n, hexnum = input().split()   
 # 16진법을 2진법으로 바꾸는 
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
    bin_to_hex = {
        '0000':'0',
        '0001':'1',
        '0010':'2',
        '0011':'3',
        '0100':'4',
        '0101':'5',
        '0110':'6',
        '0111':'7',
        '1000':'8',
        '1001':'9',
        '1010':'A',
        '1011':'B',
        '1100':'C',
        '1101':'D',
        '1110':'E',
        '1111':'F',
    }
    bin_result2 = ''
    for d in hexnum:
        print(d, hex_to_bin[d])
        bin_result2 += hex_to_bin[d]
    print(bin_result2)
    
    hex_result2 = ''
    for i in range(0, len(bin_result2), 4):
        print(i, i+4, bin_result2[i:i+4])
        print(bin_to_hex[bin_result2[i:i+4]])
        hex_result2 += bin_to_hex[bin_result2[i:i+4]]
    print(hex_result2)