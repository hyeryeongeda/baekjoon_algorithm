# 크로아티아 알파벳 리스트
ccrong = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

words = input()
# 크로아티아 알파벳을 모두 한 글자로 치환
for pororo in ccrong:
    words = words.replace(pororo, '@')  # 임의의 문자 '@'로 치환

# 치환 후 남은 글자도 한 글자씩 세면 전체 개수
print(len(words))