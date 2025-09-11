s = input().strip().upper()   # 대문자로 통일
unique = list(set(s))         # 중복 없는 알파벳 집합

max_count = 0
answer = ""
for ch in unique:
    cnt = s.count(ch)         # 문자열 안에서 해당 문자 개수 세기
    if cnt > max_count:       # 더 많이 나오면 갱신
        max_count = cnt
        answer = ch
    elif cnt == max_count:    # 횟수가 같으면 물음표 처리
        answer = "?"

print(answer)
