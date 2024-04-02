import sys
sys.stdin = open('input/1860.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    # N: 손님 수
    # M, K: M초당 붕어빵 K개 생산
    N, M, K = map(int, input().split())
    time = list(map(int, input().split()))
    time.sort()
    bread = 0
    second = 0
    result = 'Possible'
    while time:
        if second > 0 and second % M == 0:
            bread += K
        while time:
            if time[0] == second:
                time.pop(0)
                bread -= 1
            else:
                break
        if bread < 0:
            result = 'Impossible'
            break
        second += 1
    print(f'#{tc} {result}')

