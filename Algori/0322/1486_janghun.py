'''
설계_
1. 완전탐색_ 경우의 수를 모두 확인
2. 알고리즘_ DFS + 백트래킹 => 시간 복잡도 확인해주기, 
-> 20! 가지치기가 많이 되는거 같은데 감이 안온다!!
-> 똑같은 로직으로 다르게 구현 할 수 있나? 
ex) 자료 구조 바꿀 수 있나, 접근법 바꿀 수 없나

1. 가지치기 : 많이 된다. (중복제거로 인해서)
'''

import sys
sys.stdin = open("input (2).txt")

def dfs(cnt, sum_height):
    global ans
    # 기저 조건
    # 1. 키의 합이 B 이상이면 종료
    #   -> 현재까지 쌓은 탑의 높이
    if sum_height >= B:
        # 제일 높이가 낮은 탑이 정답
        # 최소 탑의 높이는 재귀호출 함수들이 동시에 사용함 -> 전역변수로 사용
        ans = min(ans, sum_height)
        return
    # 2. 모든 점원이 탑을 쌓는데 고려가 되었다면
    #   -> 현재까지 쌓은 점원의 수
    if cnt == N:
        return
    

    # 재귀 호출
    # 쌓는다
    dfs(cnt + 1, sum_height + arr[cnt])
    # 안쌓는다
    dfs(cnt + 1, sum_height)

T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = int(1e9)
    dfs(0,0)
    print(f'#{tc} {abs(ans-B)}')