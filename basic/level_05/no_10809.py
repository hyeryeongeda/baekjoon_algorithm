S = input()
dat = [-1] * 26  # a~z 처음 등장 위치 저장

for i in range(len(S)):
    idx = ord(S[i]) - 97  # 알파벳 → 0~25 숫자
    if dat[idx] == -1:   # 아직 기록 안된 경우에만 저장
        dat[idx] = i

print(*dat)