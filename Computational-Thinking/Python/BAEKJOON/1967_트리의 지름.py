import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def DFS(start, total):
    global mx
    left = right = 0
    for route, distance in tree[start]:
        r = DFS(route, distance)
        if left <= right:
            left = max(left, r)
        else:
            right = max(right, r)
    mx = max(mx, left + right)
    return max(left + total, right + total)

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    parent, child, distance = map(int, input().split())
    tree[parent].append([child, distance])
mx = 0
DFS(1, 0)
print(mx)