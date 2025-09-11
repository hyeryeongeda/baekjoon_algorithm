K = list(input().split())
a = K[0]
b = K[1]
A = a[::-1]
B = b[::-1]
if A> B:
    print(A)
else:
    print(B)

# 이런 방법도 있따;;
# a,b=map(str,input().split())
# print(max(int(a[::-1]),int(b[::-1])))