import sys
sys.stdin = open('SWEA.input/3143.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    # A: 전체 텍스트 B: 찾을 텍스트
    A, B = map(str, input().split())
    # cnt: 키를 눌러야 하는 횟수
    
    cnt = len(A)
    
    cnt -= A.count(B)*(len(B)-1)

    print(f'#{tc} {cnt}')