n = int(input())                  # 사람 수
p = list(map(int, input().split()))   # 각 사람이 돈 인출하는 데 걸리는 시간
p.sort()                              # 작은 시간부터 정렬

waiting_time = 0                                # 지금까지의 누적 합 (앞사람들 포함)
total_time = 0                                # 최종 정답(모든 사람 대기 시간의 합)

for t in p:
    waiting_time += t       # 이번 사람까지 기다린 시간
    total_time += waiting_time  # 그 사람의 실제 대기 시간 합산

print(total_time)


# waiting_time
# 지금까지 처리한 사람들의 시간을 누적해서 더한 값
# 즉, "앞 사람들 때문에 기다려야 하는 시간"을 포함한 현재 사람의 대기 시간
# 예를 들어 정렬된 시간이 [1,2,3]일 때:
# 첫 번째 사람: waiting_time = 1
# 두 번째 사람: waiting_time = 1+2 = 3
# 세 번째 사람: waiting_time = 3+3 = 6