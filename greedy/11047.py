# 입력: 첫 줄 N(동전종류), K(금액)
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]  # N줄에 걸친 동전 가치

# 보통 입력이 오름차순이지만, 안전하게 내림차순 정렬
coins.sort(reverse=True)

count = 0
for c in coins:
    if c > K:
        continue
    count += K // c   # 이 동전으로 최대 몇 개 쓰는지
    K %= c            # 남은 금액

print(count)
