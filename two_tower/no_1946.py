import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    people = [list(map(int,input().split())) for _ in range(N)]
    people.sort()

    one_top = people[0][1] # 1차 1등 
    passed = 1 # 합격자 수 일단 면접 1등은 걍 합격임
    for i in people[1:]: 
        if i[1] < one_top:
            passed += 1
            one_top=i[1]
    print(passed)
