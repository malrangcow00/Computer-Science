import sys
input = sys.stdin.readline

N, M = map(int, input().split())
P = sum(map(int, input().split())) % M
if not P:
    print(1)
else:
    print(0)
