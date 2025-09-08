import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    line = input().rstrip('\n')          # 개행 제거
    words = line.split()                 # 공백 기준 단어 분리
    reversed_words = [word[::-1] for word in words]  # 각 단어 뒤집기
    print(' '.join(reversed_words))      # 공백으로 합쳐 출력