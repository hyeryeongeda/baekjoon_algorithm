X = int(input().strip())

k = 1
while k * (k + 1) // 2 < X:
    k += 1

prev_sum = (k - 1) * k // 2
idx = X - prev_sum  # 1-based

if k % 2 == 1:  # 홀수층
    num = k - idx + 1
    den = idx
else:           # 짝수층
    num = idx
    den = k - idx + 1

print(f"{num}/{den}")