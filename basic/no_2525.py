A, B = map(int, input().split())  # 현재 시, 분
C = int(input())                  # 필요한 조리 시간 (분)

# 전체 분으로 환산
total = A * 60 + B + C

# 하루(24시간 = 1440분) 기준으로 나머지
total %= 24 * 60

# 다시 시, 분으로 변환
hour = total // 60
minute = total % 60

print(hour, minute)