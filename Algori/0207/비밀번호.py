T = 10
for tc in range(1, T+1):
    N, testcase = input().split()
    N = int(N)
    testcase = list(testcase)
    i = 0
    while i < len(testcase)-1:
        if testcase[i] == testcase[i+1]:
            testcase.pop(i)
            testcase.pop(i)
            i -= 1
        else:
            i += 1
    print(f'#{tc}',''.join(testcase))






