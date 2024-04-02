import sys
sys.stdin = open('input/5208.txt', 'r')

def f(x):
    # x 는 현재 지점.
    for i in range(x+1, x+arr[x]+1):  # 충전하여 갈 수 있는 모든 지점을 확인한다.
        if dp[i] == -1:  # 충전하여 도달한 적이 없을 때만을 따진다. / -1이 아닌 값이 있다면, 그 값은 이미 최소 충전으로 도달한 횟수를 띄고 있는 것이다.
            dp[i] = dp[x] + 1  # dp[x]는 현재 지점의 최소충전횟수이다. 여기에 + 1..
            if dp[N-1] != -1:  # 이러면 연산횟수가 줄어들까 싶어서 해봄
                return

for tc in range(1, int(input())+1):
    arr = list(map(int, input().split()))
    N = arr.pop(0)

    # dp는 해당 지점에서 최소 충전횟수를 뜻한다.
    # 지점이 -1이면 아직 충전을 통하여 도달한 적이 없다.
    dp = [-1] * 2 * N

    i = 0
    while dp[N-1] == -1:  # 기저조건은 도착지점(dp[N-1])의 최소충전횟수가 발견될때까지 이다.
        f(i)  # 각 지점으로부터의 갈 수 있는 거리를 따져본다.
        i += 1

    print(f'#{tc} {dp[N-1]}')