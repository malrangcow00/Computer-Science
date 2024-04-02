import sys
sys.stdin = open('input/1953.txt', 'r')

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    prt = [list(map(int, input().split())) for _ in range(N)]
