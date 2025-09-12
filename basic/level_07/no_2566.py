woodz = [list(map(int, input().split())) for _ in range(9)]
max_woodz = max(max(row) for row in woodz)

for i in range(9):
    for j in range(9):
        if woodz[i][j] == max_woodz:
            print(max_woodz)
            print(i+1, j+1)
