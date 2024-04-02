import sys
input = sys.stdin.readline

N = int(input())
prices = [0] + list(map(int, input().split()))
dp = [0] * (N+1)
dp[1] = prices[1]
for i in range(2, N+1):
    dp[i] = prices[i]
    for j in range(1, i//2+1):
        dp[i] = max(dp[i], dp[j] + dp[i-j])
print(dp[N])