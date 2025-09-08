n = int(input())   # 숫자 개수
stack = []

for _ in range(n):
    num = int(input())

    if num == 0:
        stack.pop()      # 최근 숫자 제거
    else:
        stack.append(num)  # 새로운 숫자 추가

print(sum(stack))  # 남은 숫자 모두 합산