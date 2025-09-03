N = int(input())               # 숫자의 개수 입력
numbers = []                   # 빈 리스트 준비

for _ in range(N):             # N번 반복하면서 입력 받기
    num = int(input())
    numbers.append(num)         # 리스트에 넣기

numbers.sort()                  # 오름차순 정렬

for n in numbers:               # 하나씩 출력
    print(n)
    