import sys
input = sys.stdin.readline

N, K = map(int, input().split())
result = 1
i = 0
while i < K:
    result *= N-i
    result //= i+1
    i += 1
print(result)