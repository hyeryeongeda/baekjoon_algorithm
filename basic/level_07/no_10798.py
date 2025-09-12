woodz = [input() for _ in range(5)]

for i in range(15):                # 최대 길이가 15이므로 인덱스 0~14까지 돌린다
    for wood in woodz:             # 5줄을 차례대로 확인
        if i < len(wood):          # 현재 줄이 i번째 글자를 가지고 있으면
            print(wood[i], end='') # 그 글자를 출력 (줄바꿈 없이 붙여쓰기)