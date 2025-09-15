import sys
input =sys.stdin.readline
N, B = map(int, input().split())

hanroro = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"  

gold_fish = []
while N > 0:
    gold_fish.append(hanroro[N % B]) 
    N //= B         

print(''.join(reversed(gold_fish)))
