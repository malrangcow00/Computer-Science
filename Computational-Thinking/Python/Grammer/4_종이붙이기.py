# f(x) = f(x-10) + 2 * f(x-20)

dp = [0] * 301

# 기저조건
dp[10] = 1
dp[20] = 3

# f(x) = f(x-10) + 2 * f(x-20)
for x in range(30, 301, 10):
    dp[x] = dp[x - 10] + 2 * dp[x-20]

T = int(input())
for tc in range(1, T+1):
    # 입력
    N = int(input())

    # 로직
    answer = dp[N]

    # 출력
    print(f'#{tc} {answer}')