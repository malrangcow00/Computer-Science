from sys import stdin

N, M = map(int, stdin.readline().split())

basket_list = []

for i in range(1, N+1):
    basket_list.append(i)
    
for i in range(M):
    first, last = map(int, stdin.readline().split())
    if first-2 == -1:
        basket_list[first-1:last] = basket_list[last-1::-1]
    else:
        basket_list[first-1:last] = basket_list[last-1:first-2:-1]
    
print(*basket_list)