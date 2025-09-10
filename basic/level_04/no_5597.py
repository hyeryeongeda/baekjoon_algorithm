import sys
input =sys.stdin.readline
seen = [False] * 31  

for _ in range(28):
    seen[int(input())] = True

for i in range(1, 31):
    if not seen[i]:
        print(i)
