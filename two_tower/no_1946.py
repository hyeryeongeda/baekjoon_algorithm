import sys

input = sys.stdin.readline

def solution():
    T = int(input())
    dat = [0]*100001
    for _ in range(T):
        N = int(input())
        for _ in range(N):
            a, b = map(int, input().split())
            dat[a] = b
        min_val = dat[1]
        res = 1
        for i in range(2, N+1):
            if dat[i] < min_val:
                min_val = dat[i]
                res += 1
        print(res)

solution()


"""import sys

def main():
    input = sys.stdin.readline
    t = int(input())
    out_lines = []

    for _ in range(t):
        n = int(input())
        # doc_rank가 i일 때의 interview_rank를 저장할 배열
        inter = [0] * (n + 1)

        for _ in range(n):
            doc, iv = map(int, input().split())
            inter[doc] = iv

        # 서류 1등부터 훑으면서 면접 최소값 갱신
        cnt = 0
        min_iv = 10**9
        for doc in range(1, n + 1):
            if inter[doc] < min_iv:
                cnt += 1
                min_iv = inter[doc]

        out_lines.append(str(cnt))

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()"""
