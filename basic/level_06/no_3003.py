arr = [1,1,2,2,2,8]
put = list(map(int, input().split()))
hanroro = []

for i in range(6):
    hanroro.append(arr[i]-put[i])

print(*hanroro)