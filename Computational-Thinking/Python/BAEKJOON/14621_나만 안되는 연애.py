import sys
input = sys.stdin.readline

N, M = map(int, input().split())
school = input().split()
roads = [[] for _ in range(N+1)]
print(roads)
for _ in range(M):
    u, v, d = map(int, input().split())
    roads[u].append([v, d])

print(roads)