# 리스트버전

n = int(input())   # 테스트케이스 개수

for _ in range(n):
    s = input()
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



# T = int(input())
# for _ in range(T):
#     s = input().strip()
#     cnt = 0
#     valid = True

#     for ch in s:
#         if ch == '(':
#             cnt += 1
#         else:  # ch == ')'
#             cnt -= 1
#             if cnt < 0:  # 닫는 괄호가 더 많아지면 실패
#                 valid = False
#                 break

#     if cnt != 0:   # 다 끝났는데 짝이 안 맞음
#         valid = False

#     print("YES" if valid else "NO")


