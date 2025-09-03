# import sys 안쓰면 시간초과 뜨는 문제
import sys
input = sys.stdin.readline 

n = int(input())
sticks = [int(input()) for _ in range(n)]

count = 0
max_height = 0

# 오른쪽에서 왼쪽으로 확인
for h in reversed(sticks):
    if h > max_height:
        count += 1
        max_height = h

print(count)
