meddugi_world = int(input())   # 단어의 개수 N 입력 (테스트 케이스 개수)

for i in range(meddugi_world):  # 단어 개수만큼 반복
    meddugi = input()           # 한 단어 입력
    for j in range(len(meddugi)-1):   # 단어를 처음부터 끝-1 까지 확인
        # 1. 현재 문자와 바로 다음 문자가 같으면 (연속된 글자면) → 그냥 넘어간다
        if meddugi[j] == meddugi[j+1]:
            continue

        # 2. 현재 문자와 다음 문자가 다를 때:
        #    - 만약 현재 문자가 "뒤쪽 남은 부분"에 또 나온다면
        #      → 그룹 단어 조건 위반 (끊겼던 문자가 다시 나온 경우)
        elif meddugi[j] in meddugi[j+1:]:
            meddugi_world -= 1   # 그룹 단어 개수에서 1 빼기
            break                # 더 확인할 필요 없으니 반복문 종료

print(meddugi_world)  # 최종적으로 그룹 단어의 개수를 출력
