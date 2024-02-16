# 삽입
# rear 값을 하나 증가시켜 새로운 원소를 삽입할 자리 마련
# 그 인덱스에 해당하는 배열원소 Q[rear]에 item을 저장
# 삭제
# front값을 하나 증가시켜 큐에 남아있는 첫 번째 원소로 이동
# 새로운 첫 번째 원소를 리턴함으로써 삭제와 동일한 기능함
# isEmpty() : 공백상태는 front == rear / isFull() : 포화상태는 rear == len(Q)-1

# 연산
# enQueue(item) : 큐 뒤쪽에 원소 삽입 (rear)
# deQueue(item) : 큐 앞쪽에서 원소 삭제하고 반환 (front)
'''
queue = []
queue.append(1)
queue.append(2)
queue.append(3)
# print(queue.pop(0))
# print(queue.pop(0))
# print(queue.pop(0))
while queue:
    print(queue.pop(0))
'''

'''
# 선형큐 연습문제 실습
N = 10 # 큐생성
q = [0] * 10
front = rear = -1

rear += 1 # enqueue(10)
q[rear] = 10
rear += 1 # enqueue(20)
q[rear] = 20
rear += 1 # enqueue(30)
q[rear] = 30
while front != rear: # 큐가 비어있지 않으면
    front += 1
    print(q[front])
'''

# 덱

# from collections import deque
#
# q = deque()
# q.append(1) # enqueue()
# t = q.popleft() # dequeue()
# q.append(2)
# print(q.popleft())
# print(q.popleft())

# dq = deque()
# # q = []
# for i in range(10000):
#     dq.append(i)
# print('append')
# while dq:
#     dq.popleft()
# print('end')

T = int(input())
N = list(map(int, input().strip()))
print(sum(N))