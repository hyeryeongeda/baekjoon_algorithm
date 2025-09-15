m = int(input()) 
n = int(input())
num = 0  
arr = [] 

for i in range(m, n + 1): 
    for j in range(2, i): 
        if i % j == 0: 
            num += 1 
            break 
    if num == 0 and i != 1:
        arr.append(i) 
    num = 0 

if len(arr) == 0: 
    print(-1) 
else: 
    print(sum(arr))
    print(min(arr)) 