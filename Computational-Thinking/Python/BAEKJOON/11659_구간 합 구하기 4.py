import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = [0] + list(map(int, input().split()))
dp = [0] * (N+1)
dp[1] = nums[1]
for i in range(2, N+1):
    dp[i] = dp[i-1] + nums[i]
for _ in range(M):
    s, e = map(int, input().split())
    print(dp[e]-dp[s-1])