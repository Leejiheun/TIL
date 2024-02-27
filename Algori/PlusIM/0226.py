arr=[[1,2,3],
     [4,5,6],
     [7,8,9]]

# 
# for i in zip(arr[0],arr[1],arr[2]):
#     print(list(i))
# 
# for i in zip(*arr):
#     print(list(i))
# 
# ret=list(map(list,zip(*arr)))

arr=list(map(list,zip(*arr)))
for i in range(3):
    for j in range(3):
        print(arr[i][j],end=' ')
    print()

# zip 함수
# 순회 가능한 객체를 인자로 받고,
# 각각의 요소를 잘라서 튜플을 원소로 하는 zip객체를 반환!!
a='12345'
b='asdfg'
c='qwert'

# ret=zip(a,b)
# print(ret)
# print(list(ret))


# for i in zip(a,b,c):
#     print(i)
# 
# for i in zip(a,b,c):
#     print(list(i))
# 
# for y,x,z in zip(a,b,c):
#     print(y,x,z)