import sys
input =sys.stdin.readline
N = int(input())

bang = 1     
mazimac = 1        

while N > mazimac:       
    mazimac += 6 * bang  
    bang += 1

print(bang)