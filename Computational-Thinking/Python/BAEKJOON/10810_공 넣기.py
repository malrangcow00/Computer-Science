from sys import stdin

N, M = map(int, input().split())

empty_list = [0] * N

for times in range(M):
    i, j, k = map(int, stdin.readline().split())
    for num_basket in range(i-1, j):
        empty_list[num_basket] = k
        
print(*empty_list)