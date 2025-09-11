T = int(input())
for tc in range(T):
    S = input().split()
    k = int(S[0])
    ment = []
    S = list(str(S[1]))
    for i in range(len(S)):
        ment += k*S[i]
    
    print(*ment, sep='')