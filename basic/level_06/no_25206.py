hakssi = []
for _ in range(20):
    hakssi.append(input().split())

hakjum_lineup = {
    'A+': 4.5, 'A0': 4.0,
    'B+': 3.5, 'B0': 3.0,
    'C+': 2.5, 'C0': 2.0,
    'D+': 1.5, 'D0': 1.0,
    'F' : 0.0
}

punghakjum = 0.0  # 학점 * 평점 합
sumhakjum = 0.0  # 학점 합

for i in range(20):
    subject, hakjum_munja, grade = hakssi[i]
    hakjum = float(hakjum_munja)

    if grade == 'P':           
        continue

    punghakjum += hakjum * hakjum_lineup[grade]
    sumhakjum += hakjum


gunhakjum = 0.0 if sumhakjum == 0 else punghakjum / sumhakjum
print(f"{gunhakjum:.6f}")
