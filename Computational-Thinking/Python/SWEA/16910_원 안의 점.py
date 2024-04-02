import sys
sys.stdin = open('SWEA.test.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    for y in range(-N-1, N+1):
        for x in range(-N-1, N+1):
            if x**2 + y**2 <= N**2:
                cnt += 1
    print(f'#{tc} {cnt}')