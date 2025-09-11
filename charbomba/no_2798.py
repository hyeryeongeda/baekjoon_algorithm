# 입력 받기
N, M = map(int, input().split())       # N: 카드 개수, M: 목표 숫자
cards = list(map(int, input().split()))  # 카드에 적힌 숫자들 (리스트)

# 가장 좋은 카드 합을 저장할 변수 (처음에는 0으로 시작)
best_card = 0

# 3장의 카드를 뽑기 위해 3중 반복문 사용
for i in range(N - 2):                 # 첫 번째 카드 (0번째부터 N-3번째까지)
    for j in range(i + 1, N - 1):      # 두 번째 카드 (첫 번째 카드 이후부터)
        for k in range(j + 1, N):      # 세 번째 카드 (두 번째 카드 이후부터)
            
            # 세 장의 카드 합 구하기
            hanroro = cards[i] + cards[j] + cards[k]
            
            # 합이 M을 넘지 않으면서, 지금까지의 최고 기록보다 크면 갱신
            if hanroro <= M and hanroro > best_card:
                best_card = hanroro

# 최종적으로 얻은 가장 큰 합 출력
print(best_card)

"""
N, M을 입력받는다.
N은 카드 개수.
M은 넘지 말아야 할 최대 합.
카드 숫자들을 리스트로 저장한다.
best_card = 0 → 지금까지 찾은 “가장 좋은 카드 합”을 저장하는 변수.
세 겹의 for문을 돌면서 카드 3장을 모두 뽑아본다.
i < j < k 조건을 강제로 걸어서 같은 카드를 두 번 뽑지 않도록 한다.
카드 3장의 합을 hanroro 변수에 저장한다.
그 합이 M을 넘지 않으면서, 기존의 best_card보다 크면 갱신한다.
모든 경우를 다 탐색한 뒤, 가장 좋은 값(best_card)을 출력한다.
"""