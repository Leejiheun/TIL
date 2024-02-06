num = int(input())
cnt = 0

for i in range(num):
    word = input()
    emt = []
    
    if len(word) == 1:
        cnt += 1
    else:
        for j in range(len(word)):
            if word[j] not in word:
                emt.append(word[j])
            else:
                if word[j-1] != word[j]:
                    cnt = 0
        cnt += 1
    print(cnt)