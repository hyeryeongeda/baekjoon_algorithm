import sys
input = sys.stdin.readline

n = int(input())
s, out = [], []

for _ in range(n):
    c = input().split()
    if c[0] == 'push':
        s.append(int(c[1]))
    elif c[0] == 'pop':
        out.append(str(s.pop() if s else -1))
    elif c[0] == 'size':
        out.append(str(len(s)))
    elif c[0] == 'empty':
        out.append('0' if s else '1')
    else:  # top
        out.append(str(s[-1] if s else -1))

print('\n'.join(out))
