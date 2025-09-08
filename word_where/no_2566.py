import sys
input = sys.stdin.read

nums = list(map(int, input().split()))

mx = max(nums)
idx = nums.index(mx)            # 최댓값의 첫 등장 위치(0-based)
r, c = idx // 9 + 1, idx % 9 + 1  # 1-based로 변환

print(mx)
print(r, c)
