H,M=map(int,input().split())

if H == 0:
    H = 24

time=( H * 60 ) + M - 45
H = (time // 60) % 24
M = time % 60

print(H, M)