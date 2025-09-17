import sys
input = sys.stdin.readline
stack = []
N = int(input())

for _ in range(N):
    input_list = list(input().split())
    
    # 'push' 명령: stack에 값 추가
    if input_list[0] == 'push':
        stack.append(input_list[1])  # input_list[1]은 push로 추가할 값
    
    # 'pop' 명령: stack에서 가장 최근 값 꺼내기
    elif input_list[0] == 'pop':
        # 스택이 비어있지 않으면 pop, 비어 있으면 -1 출력
        print(stack.pop() if stack else -1)
    
    # 'size' 명령: stack의 크기 출력
    elif input_list[0] == 'size':
        print(len(stack))
    
    # 'empty' 명령: stack이 비어 있으면 1, 아니면 0 출력
    elif input_list[0] == 'empty':
        # stack이 비어 있으면 1, 아니면 0
        print(0 if stack else 1)
    
    # 'top' 명령: stack의 맨 위 값 출력
    elif input_list[0] == 'top':
        # stack이 비어 있으면 -1, 아니면 stack[-1] 출력
        print(stack[-1] if stack else -1)



        