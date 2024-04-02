import sys
input = sys.stdin.readline

# 대각선 이동이 가능 !! ...
X, Y, D, T = map(float, input().split())
distance = (X**2 + Y**2)**0.5
# 점프 조건
# 1. 일단 점프의 효율이 걷기 보다 좋아야 함.
# 2. 남은 거리가 점프 한 번의 시간 보다 적어야 함.
# 점프 왜함 ?
if D/T <= 1 or distance <= T:
    print(distance)
# JUMP
else:
    result = 0
    # 효율이 좋으니까 일단 점프해
    while distance >= 2*D:
        distance -= D
        result += T
    # 남은 거리 < 2D
    # 점프 두번으로는 무조건 갈 수 있는 거리가 남았다...
    # 1. 점프 두 번: 2*T
    # 2. 점프 한 번 하고 남은 거리 걷기: T + abs(distance-D)
        # 점프 한번 보다 거리가 적게 남은 경우...
        # 목적지를 지나, 걸어서 추가된 거리를 돌아오더라도 점프 두 번 보다 더 빠른 경우가 존재...
    # 3. 모든 조건을 만족하면서 남은 거리를 걷는 시간이 위의 경우들 보다 적은 경우: distance
    tmp = min(2*T, T + abs(distance-D), distance)
    result += tmp
    print(result)
