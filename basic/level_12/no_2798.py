N, M = map(int, input().split())      
cards = list(map(int, input().split())) 

best_hap = 0

for i in range(N - 2):                 
    for j in range(i + 1, N - 1):      
        for k in range(j + 1, N):     
            
            bbh = cards[i] + cards[j] + cards[k]
            
            if bbh <= M and bbh > best_hap:
                best_hap = bbh

print(best_hap)