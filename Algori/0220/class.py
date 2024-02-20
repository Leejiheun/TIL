# 이진 트리
'''
**각 노드가 자식 노드를 최대한 2개 까지만 가질 수 있는 트리**
1) 왼쪽 자식 노드 2) 오른쪽 자식 노드

특성 : 레벨 i 에서의 노드의 최대 개수는 2**i개

# 포화 이진 트리
모든 레벨에 노드가 포화상태로 차 있는 이진 트리

# 완전 이진 트리
빈 자리가 없는 이진 트리

# 편향 이진 트리
한 쪽 방향의 자식 노드만을 가진 이진 트리
1) 왼쪽 편향 이진 트리 2) 오른쪽 편향 이진 트이
'''

# 이진 트리_순회
'''
3가지 기본적인 순회방법
- 전위순회(VLR) : 부모 왼 오 (preorder)
- 중위순회(LVR) : 왼 부 오 (inorder)
- 후위순회(LRV) : 왼 우 부 (postorder)
'''
# def preorder_traverse(T): # 전위순회
#     if T:
#         visit(T)
#         preorder_traverse(T.left)
#         preorder_traverse(T.right)



# 이진 트리의 표현 _ 배열







# 연습문제
'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
def pre_order(T): # T에 방문했으면
    if T:
        print(T, end = ' ')
        pre_order(left[T])
        pre_order(right[T])

N = int(input()) # 1번부터 N번까지인 정점
E = N-1  # 간선수
arr = list(map(int, input().split()))
left = [0] * (N+1)  # 부모를 인덱스로 왼쪽자식번호 저장
right = [0] * (N+1) # 오른쪽 자식
par = [0] * (N+1)

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
# for i in range(0, E*2, 2):
#     p, c = arr[i], arr[i * 2 + 1]
    if left[p] == 0: # 왼쪽자식이 없으면
        left[p] = c
    else:
        right[p] = c
    par[c] = p

c = N
while par[c] != 0: # 부모가 있으면
    c = par[c]    # 부모를 새로운 자식으로 두고
root = c          # 더이상 부모가 없으면 root
print(root)
pre_order(root)