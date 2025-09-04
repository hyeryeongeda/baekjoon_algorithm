def score(line):
    contin = 0
    total = 0
    for chi in line:
        if chi == 'O':
            contin += 1
            total += contin
        else:  
            contin = 0
    return total

n = int(input())
for _ in range(n):
    line = input().strip()
    print(score(line))