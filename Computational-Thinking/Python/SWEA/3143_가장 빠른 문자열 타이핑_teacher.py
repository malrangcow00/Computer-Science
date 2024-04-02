import sys
sys.stdin = open('SWEA.input/3143.txt', 'r')

T = int(input())
 
def BruteForce(t, p):
    N = len(t)
    M = len(p)
 
    # 카운트 변수
    cnt = 0
 
    skipped = 0
    for i in range(N - M + 1):
        if skipped:
            skipped -= 1
            continue
        if p == t[i:i + M]:
            cnt += 1
            skipped = M - 1
 
    return cnt
 
 
for tc in range(1, T + 1):
    # 입력
    A, B = input().split()
 
    # 메인
    cnt = BruteForce(A, B)
    answer = len(A) - (len(B) * cnt) + cnt
 
    # 출력
    print(f"#{tc} {answer}")
