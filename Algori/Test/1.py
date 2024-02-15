# 알고리즘 스터디
new_list = []
for _ in range(10):
    T = int(input())
    a = T % 42
    if a not in new_list:
        new_list.append(a)
print(len(new_list))