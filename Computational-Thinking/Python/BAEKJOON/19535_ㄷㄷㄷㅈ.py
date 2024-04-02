import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N = int(input())
edges = []
degree = [0 for _ in range(N+1)]

for _ in range(N-1):
    u, v = map(int, input().split())
    edges.append([u, v])
    degree[u] += 1
    degree[v] += 1

cnt_D = 0
cnt_G = 0

for edge in edges:
    # 앞 뒤 (노드의 엣지수 - 1)을 서로 곱하면 두 노드를 포함한 D-트리의 개수를 구할 수 있다 !!! 
    cnt_D += (degree[edge[0]]-1) * (degree[edge[1]]-1)

for idx in range(1, N+1):
    if degree[idx] >= 3:
        cnt_G += degree[idx]*(degree[idx]-1)*(degree[idx]-2)//6

# print(f'cnt_D : {cnt_D}, cnt_G : {cnt_G}')

# D-트리와 G-트리의 개수를 비교
if cnt_D > 3 * cnt_G:
    print('D')
elif cnt_D < 3 * cnt_G:
    print('G')
else:
    print('DUDUDUNGA')
