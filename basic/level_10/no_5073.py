while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:   # 종료 조건
        break

    sides = sorted([a, b, c])  # 오름차순 정렬
    if sides[2] >= sides[0] + sides[1]:
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a == b or a == c or b == c:
        print("Isosceles")
    else:
        print("Scalene")
