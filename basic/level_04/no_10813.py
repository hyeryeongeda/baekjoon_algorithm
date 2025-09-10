N, M = map(int, input().split())
dat = [0] * N
for k in range(N):
    dat[k] = k + 1          

for _ in range(M):
    i, j = map(int, input().split())
    i -= 1                   
    j -= 1

    tmp = dat[i]
    dat[i] = dat[j]
    dat[j] = tmp

print(*dat)

"""import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(range(1, N + 1))

for _ in range(M):
    i, j = map(int, input().split())
    arr[i - 1], arr[j - 1] = arr[j - 1], arr[i - 1]

print(*arr)"""