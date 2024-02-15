T = 10
for tc in range(1, T+1):
    N = int(input())
    fx = input()
    st = []
    postfix = ''

    for tk in fx:
        if tk == '+':
            while st:
                postfix += st.pop()
            st.append(tk)
        else:
            postfix += tk
    while st:
        postfix += st.pop()

    for tk in postfix:
        if tk == '+':
            t1 = st.pop()
            t2 = st.pop()
            t3 = int(t1) + int(t2)
            st.append(t3)
        else:
            st.append(tk)
    print(f'#{tc} {st[0]}')





for x in range(10):
    n = int(input())
    st = []
    postfix = ''
    fx = input()

    for tk in fx:
        if tk == '+':
            while st:
                postfix += st.pop()
            st.append(tk)
        else:
            postfix += tk
    while st:
        postfix += st.pop()

    for tk in postfix:
        if tk == '+':
            t1 = st.pop()
            t2 = st.pop()
            t3 = int(t1) + int(t2)
            st.append(t3)
        else:
            st.append(tk)
    print(f'#{x+1} {st[0]}')