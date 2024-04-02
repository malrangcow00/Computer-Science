import sys
input = sys.stdin.readline

K = int(input())
order = list(map(int, input().split()))
tree = [[] for _ in range(K)]

def cut(order, i):
    mid = len(order) // 2
    tree[i].append(order[mid])

    if len(order) == 1:
        return

    cut(order[:mid], i+1)
    cut(order[mid+1:], i+1)

cut(order, 0)

for _ in tree:
    print(*_)