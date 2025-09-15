import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
total = 0
ans = N + 1  # 불가능 표시용 큰 값

for right in range(N):
    total += arr[right]

    # 조건을 만족하는 동안 최대한 왼쪽을 줄여서 최소 길이 갱신
    while total >= S:
        cur_len = right - left + 1
        if cur_len < ans:
            ans = cur_len
        total -= arr[left]
        left += 1

print(0 if ans == N + 1 else ans)
