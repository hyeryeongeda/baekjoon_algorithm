import sys

input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

window = sum(arr[:K])
ans = window

for i in range(K, N):
    window += arr[i] - arr[i - K]
    if window > ans:
        ans = window

print(ans)