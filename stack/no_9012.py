n = int(input())   # 테스트케이스 개수

for _ in range(n):
    s = input().strip()
    stack = []
    valid = True

    for ch in s:
        if ch == '(':
            stack.append(ch)
        else:  # ')'
            if stack:   # 스택이 비어있지 않으면 pop
                stack.pop()
            else:       # 비어있는데 ')'가 나오면 NO
                valid = False
                break

    if stack:   # 스택에 남아 있으면 NO
        valid = False

    print("YES" if valid else "NO")
