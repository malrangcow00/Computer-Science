import sys
sys.stdin = open('input/13994.txt', 'r')

T = int(input()) # 1<= T <= 1000
for tc in range(1, T+1):
    N = int(input()) # N: 버스의 개수
    cnt = [0] * 1001
    for _ in range(N):
        # 버스 타입과 출발, 도착 정류장 번호
        type, *station = map(int, input().split())
        # 1: 일반 버스
        if type == 1:
            for i in range(station[0], station[1]+1):
                cnt[i] += 1
        # 2: 급행 버스
        elif type == 2:
            for i in range(station[0], station[1]+1, 2):
                cnt[i] += 1
        # 3: 고속 버스
        else:
            if station[0] % 2 == 0:
                for i in range(station[0], station[1]+1):
                    if i % 4 == 0:
                        cnt[i] += 1
            else:
                for i in range(station[0], station[1]+1):
                    if i % 3 == 0 and i % 10 != 0:
                        cnt[i] += 1
    print(f'#{tc} {max(cnt)}')