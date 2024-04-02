import sys
input = sys.stdin.readline

N, K = map(int, input().split())
templerature = list(map(int, input().split()))
sum_templerature = [0] * (N+1)
for i in range(1, N+1):
    sum_templerature[i] = sum_templerature[i-1] + templerature[i-1]
    mx = -float('inf')
for i in range(K, N+1):
    mx = max(mx, sum_templerature[i]-sum_templerature[i-K])
print(mx)

