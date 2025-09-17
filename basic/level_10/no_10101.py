a = int(input())
b = int(input())
c = int(input())

samhap = a + b + c

if a == 60 and b == 60 and c == 60:
    print("Equilateral")
elif samhap == 180 and (a == b or a == c or b == c):
    print("Isosceles")
elif samhap == 180 and (a != b and a != c and b != c):
    print("Scalene")
else:
    print("Error")