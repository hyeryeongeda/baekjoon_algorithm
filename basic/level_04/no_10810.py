N,M = map(int,input().split())
dat = [0] * N
for _ in range(M):
    i,j,k = map(int,input().split())
    for a in range(i,j+1):
        dat[a-1] = k

print(*dat)        