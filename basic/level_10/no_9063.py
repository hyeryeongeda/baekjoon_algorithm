N = int(input())
x = []
y = []

for _ in range(N):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)

square_size = (max(x) - min(x)) * (max(y) - min(y))
print(square_size)