import sys
sys.stdin = open('SWEA.input/3143.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    # A: 전체 텍스트 B: 찾을 텍스트
    A, B = map(str, input().split())
    # cnt: 키를 눌러야 하는 횟수
    
    cnt = len(A)

    skipped = 0
    for i in range(len(A)):
        if skipped != 0:
            skipped -= 1
            continue
        if B[0] == A[i]:
            for j in range(len(B)):
                if i+j < len(A) and B[j] == A[i+j]:
                    if j == len(B)-1:
                        cnt -= len(B)-1
                        skipped = len(B)-1
                else:
                    break

    print(f'#{tc} {cnt}')