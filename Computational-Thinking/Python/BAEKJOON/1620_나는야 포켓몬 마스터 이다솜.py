import sys

N, M = map(int, sys.stdin.readline().split())
poke_dict = {}
for _ in range(1, N+1):
    poke_dict[sys.stdin.readline().strip()] = _
index_poke_dict = {value:key for key, value in poke_dict.items()}
for _ in range(M):
    Q = sys.stdin.readline().strip()
    if Q.isdigit():
        print(index_poke_dict.get(int(Q)))
    else:
        print(poke_dict[Q])