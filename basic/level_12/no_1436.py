import sys
input = sys.stdin.readline

n = int(input())  # 입력받은 n
num = 666          # 첫 번째 숫자 666
count = 0          # '666'이 포함된 숫자 개수를 셀 변수

while True:
    if '666' in str(num):  # num에 '666'이 포함되어 있으면
        count += 1         # count를 하나 증가
        if count == n:     # 원하는 개수만큼 찾으면
            break          # 반복 종료
    num += 1  # num을 1씩 증가시킴

print(num)  # 마지막으로 찾은 '666'이 포함된 숫자 출력
