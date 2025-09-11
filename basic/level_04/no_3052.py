# 중복 제거를 위해 set 사용하믄 된다잉
hanroro = {int(input()) % 42 for _ in range(10)}
print(len(hanroro))