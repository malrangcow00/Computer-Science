import sys

N = int(sys.stdin.readline())

arr = list(set([sys.stdin.readline().strip() for _ in range(N)]))

arr.sort()

len_arr = []
for _ in arr:
    len_arr.append((len(_), _))

len_arr.sort()

for len, word in len_arr:
    print(word)