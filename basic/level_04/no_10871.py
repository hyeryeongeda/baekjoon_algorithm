N,X = map(int,input().split())
arr = list(map(int, input().split()))
gae=[]
for i in range(N):
    if arr[i]<X:
        gae.append(arr[i])

print(*gae)