import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    H, W = map(int, input().split())
    for _ in range(H):
        print(input().rstrip()[::-1])
