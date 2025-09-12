import sys
input = sys.stdin.readline

N = int(input())                 # 색종이 개수
paper = [[0]*100 for _ in range(100)]  # 100×100 도화지 (전부 0으로 초기화)

for _ in range(N):
    x, y = map(int, input().split())
    # (x, y)를 시작점으로 10×10 칸을 1로 채움
    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[i][j] = 1

# 전체 도화지에서 1의 개수 세기
area = 0
for i in range(100):
    for j in range(100):
        area += paper[i][j]

print(area)
