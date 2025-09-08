T = int(input())
for _ in range(T):
    s = input().strip()
    cnt = 0
    valid = True

    for ch in s:
        if ch == '(':
            cnt += 1
        else:  # ch == ')'
            cnt -= 1
            if cnt < 0:  # 닫는 괄호가 더 많아지면 실패
                valid = False
                break

    if cnt != 0:   # 다 끝났는데 짝이 안 맞음
        valid = False

    print("YES" if valid else "NO")