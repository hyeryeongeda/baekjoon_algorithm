# 약수 구하기
N, K =  map(int, input().split())

yak_cnt=0

for i in range(1,N+1):
    if N%i ==0:
        yak_cnt +=1
        if yak_cnt == K:
            print(i)
            break
else:
    print(0)