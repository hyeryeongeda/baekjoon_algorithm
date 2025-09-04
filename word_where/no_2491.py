def score(line):
    n = len(line)
    incr = decr = ans = 1
    for i in range(n - 1):
        if line[i] <= line[i + 1]:
            incr += 1
        else:
            incr = 1
        if line[i] >= line[i + 1]:
            decr += 1
        else:
            decr = 1
        ans = max(ans, incr, decr)
    return ans

n = int(input())
line = list(map(int, input().split()))
print(score(line))
