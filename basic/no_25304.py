X = int(input())
N = int(input())
total_pay = 0

for _ in range(N):
    a, b = map(int, input().split()) # 줄로 받는 거
    total_pay += a * b
    
if X == total_pay:
    print('Yes')
else:
    print('No')