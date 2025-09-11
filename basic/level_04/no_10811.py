N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]  # 1부터 N까지 바구니 번호 넣기

for _ in range(M):
    i, j = map(int, input().split())
    arr[i-1:j] = reversed(arr[i-1:j])  # i~j 구간 뒤집기

print(*arr)