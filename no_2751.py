import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.read().split()))
nums.sort()
print("\n".join(map(str, nums)))