N = int(input())
result = 0

for i in range(1, N + 1):
    num = i
    while num:
        check = num % 10
        num //= 10

        if check == 3 or check == 6 or check == 9:
            result += 1
print(result)