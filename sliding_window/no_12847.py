import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

# 처음 M일 합
window = sum(arr[:M])
dondon = window

# 창문을 오른쪽으로 밀기
for i in range(M, N):
    window += arr[i] - arr[i-M]  # 들어온 값 arr[i], 나간 값 arr[i-M]
    dondon = max(dondon, window)

print(dondon)
