N = int(input())   # 목표 숫자 N을 입력받음

def digit_sum(n):
    # 숫자 n의 각 자리수를 더해서 반환하는 함수
    # 예: n=245 -> 2+4+5 = 11
    return sum(int(ch) for ch in str(n))

digit = len(str(N))   # N의 자릿수 (예: N=245 -> 3자리)
M = N - 1             # 후보 숫자를 N보다 작은 값부터 시작
result = 0            # 생성자를 저장할 변수 (없으면 0)

# 생성자는 N - (자릿수 * 9) 부터 N-1 사이에 존재할 수 있음
# 따라서 최대 digit*9번만 검사하면 충분함
for _ in range(digit * 9):
    if M < 1:         # M이 1보다 작아지면 더 이상 검사할 필요 없음
        break
    # 만약 "M + M의 각 자리수 합"이 N과 같으면
    if digit_sum(M) + M == N:
        result = M    # M은 N의 생성자, result에 저장
    M -= 1            # 다음 후보로 이동

print(result)         # 최종적으로 찾은 생성자를 출력 (없으면 0)