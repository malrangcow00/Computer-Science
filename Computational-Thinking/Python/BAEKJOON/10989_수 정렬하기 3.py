# dictionary를 이용한 방법

import sys

num_dict = {}
N = int(sys.stdin.readline())

for _ in range(N):
    i = int(sys.stdin.readline())
    if i not in num_dict.keys():
        num_dict[i] = 0
    num_dict[i] += 1

print()

num_dict = dict(sorted(num_dict.items()))

for key, value in num_dict.items():
    for i in range(value):
        print(key)

# count sort를 이용한 방법 ?