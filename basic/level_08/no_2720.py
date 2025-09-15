import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    c = int(input())
    q, c = divmod(c, 25)  
    d, c = divmod(c, 10) 
    n, c = divmod(c, 5)   
    p = c                 
    print(q, d, n, p)