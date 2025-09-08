S = []
max_len = 0
for _ in range(5):
    a = input()
    S.append(a)
    if max_len < len(a):
        max_len = len(a)

for i in range(max_len):
    for j in range(5):
        try:
            print(S[j][i], end="")
        except IndexError:
            pass