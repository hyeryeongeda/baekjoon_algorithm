import sys

input = sys.stdin.readline

n = int(input())
stack = []
out = []

for _ in range(n):
    cmd = input().split()

    if cmd[0] == '1':                 # push X
        stack.append(int(cmd[1]))
    elif cmd[0] == '2':               # pop
        out.append(str(stack.pop()) if stack else '-1')
    elif cmd[0] == '3':               # size
        out.append(str(len(stack)))
    elif cmd[0] == '4':               # empty
        out.append('1' if not stack else '0')
    elif cmd[0] == '5':               # top
        out.append(str(stack[-1]) if stack else '-1')

print('\n'.join(out))
