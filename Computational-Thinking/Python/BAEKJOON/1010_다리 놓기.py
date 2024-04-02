import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    result = 1
    i = 0
    while i < N:
        result *= M-i
        result //= i+1
        i += 1
    print(result)