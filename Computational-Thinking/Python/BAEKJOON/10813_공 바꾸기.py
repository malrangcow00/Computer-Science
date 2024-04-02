from sys import stdin

N, M = map(int, input().split())

basket_list = []

for i in range(1, N+1):
    basket_list.append(i)

for swaps in range(M):
    i, j = map(int, stdin.readline().split())
    basket_list[i-1], basket_list[j-1] = basket_list[j-1], basket_list[i-1]
        
print(*basket_list)