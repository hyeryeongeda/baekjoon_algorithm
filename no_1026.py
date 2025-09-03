n = int(input().strip())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()              # A는 오름차순
B.sort(reverse=True)  # B는 내림차순

result = 0
for i in range(n):
    result += A[i] * B[i]

# for a, b in zip(A, B):
#     result += a * b

print(result)
