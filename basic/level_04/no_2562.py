import sys
input = sys.stdin.readline

arr = [int(input()) for _ in range(9)]
mx = max(arr)
idx = arr.index(mx) + 1   

print(mx)
print(idx)