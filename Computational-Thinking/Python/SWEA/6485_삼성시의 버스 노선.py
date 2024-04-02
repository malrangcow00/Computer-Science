import sys
sys.stdin = open('input/6485.txt', 'r')

# 딕셔너리로 접근하면 없는 번호를 조회할 때 0을 출력해주지 못하므로 입력에 없는 번호를 판별하여 따로 생성해주어야 한다 (비효율적)
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = [0] * 5001
    for i in range(N):
        A, B = map(int, input().split())
        for i in range(A, B+1):
            cnt[i] += 1
    P = int(input())
    bus_stop = [int(input()) for _ in range(P)]
    print(f'#{tc}', end=' ')
    for x in bus_stop:
        print(cnt[x], end=' ')
    print()