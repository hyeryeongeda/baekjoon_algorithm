while True:
    s = input().rstrip()
    if s == '.':
        break

    stack = []
    ok = True

    for ch in s:
        if ch in '([':
            stack.append(ch)
        elif ch == ')':
            if not stack or stack.pop() != '(':
                ok = False; break
        elif ch == ']':
            if not stack or stack.pop() != '[':
                ok = False; break

    print('yes' if ok and not stack else 'no')


# import sys

# def yesorno(s) :
#     stack=list()
#     pair={ ')' : '(', ']' : '[' }
#     for char in s :
#         if char in '([' :
#             stack.append(char)
#         elif char in ")]" :
#             if not stack or stack.pop()!=pair.get(char) :
#                 return False
#     return not stack
    
# while True :
#     sentence = sys.stdin.readline().rstrip()
#     if sentence=='.' :
#         break
#     if yesorno(sentence) :
#         print("yes")
#     else :
#         print("no")