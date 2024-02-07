# 재귀호출의 기본형
def f(i, k): # i 현재 위치, k목 표
    if i == k:
        print(brr)
    else:
        brr[i] = arr[i]
        # print(arr[i])
        f(i+1, k)

arr = [10, 20, 30]
N = len(arr)
brr = [0]*N
f(0, N)

# 서로 다른 함수 호출하는 거랑 동일하게 생각하면 된다.