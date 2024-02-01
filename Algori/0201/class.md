# 순차 검색
- 일렬로 되어 있는 자료를 순서대로 검색하는 방법
  - 알고리즘이 단순해서 구현 쉽지만, 검색 대상 수가 많으면 수행시간 급격히 증가하여 비효율
- 두 가지 경우
  - 정렬되어 있지 않는 경우
    - 모든 원소 접근해서 비교
  ```python
  for i:0->N-2:
    if A(i) == key
        return i
  return -1 # 찾는 값이 없을 경우
  ```

  ```python
  def
  ```
  - 정렬되어 있는 경우
    - 어떤 자료를 계속 반복해서 검색을 할 경우, 정렬을 해놓고 검색하는게 효율적
    - 시간복잡도 : O(n)
  ```python
  def sequen(a, n, key):
    i <-0
    while i < n and a[i]<key:
      i<-i+1
    if i<n and a[i] == key:
      return i
    else:
      return -1

  for i in range(N):
    if a[i] == key:
      return i
    else:
      break
  return -1
  ```

# 이진 검색
- 자료가 정렬된 상태에서 시작
- 자료 가운데 있는 항목의 키 값과 비교해서 다음 검색위치를 결정하고 계속 진행시키는 방법
  - 자료 중앙 원소
  - 중앙 원소 값과 찾고자 하는 목표값 비교
  - 목표 중앙 원소보다 작으면 왼쪽 반에 대해 새로 검색, 크면 오른쪽 반에 대해 새로 검색 수행
  - 찾고자 하는 값을 찾을 때까지 반복
- s ~ e
- m = (s+e)//2
```python
def binary(arr, N, key):
  start = 0 # 구간 초기화
  end = N-1
  # 검색 구간이 유효하면 반복
  while start <= end:
    # 중앙 원소의 인덱스
    middle = (start + end)//2
    if arr[middle] == key # 검색성공
      return middle
    # 중앙값이 키보다 크면
    elif arr[middle] >= key:
      end = middel - 1
    else:
      start = middle + 1
  return false # 검색실패
  ```
# 선택 정렬
- 주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치 교환
  - 주어진 리스트 중 최솟값 찾고
  - 그 값을 리스트 맨 앞에 위치한 값과 교환
  - 맨 처음 위치를 제외한 나머지 리스트 대상으로 위의 과정 반복
  - 시간복잡도 : O(n**2)
```python
min_idx = 0
for j : 0 -> 4
  if A[min_adx] > A[j]
    min_adx = j
A[min_adx] <-> A[0]

min_idx = 1
for j : 1 -> 4:
  if A[min_adx] > A[j]
    min_adx = j
A[min_adx] <-> A[1]
--------
def selectionSort(A, N)
for i in range(N-1):
  min_idx = i # 맨 앞 원소를 최솟값 위치로 가줌
  for j in range(i+1, N): # 실제 최솟값 위치 검색
    if A[min_adx] > A[j]
      min_adx = j
  A[i], A[min_adx] = A[min_idx], A[i]
  ```
# 선택 정렬
```
def selection_sort(a, N):
  # 구간의 시작을 i로 정해줌, 2개의 원소가 남을 떄까지
  for i in range(N-1):
    # 구간의 최솟값 위치를 min_idx, 첫 원소를 최소로 가정
    min_idx = i
    # 실제 최솟값을 찾을 인덱스 위치 j
    for j in range(i+1, N-1):
      if a[min_idx] > a[j]:
        min_idx = j
    # 최솟값을 구간의 맨 앞으로 이동
    a[min_idx], a[i] = a[i], a[min_idx]
```
