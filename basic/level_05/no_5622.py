dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

word = input().strip()
time = 0

for ch in word:
    for i in range(len(dial)):
        if ch in dial[i]:
            time += i + 3 
print(time)