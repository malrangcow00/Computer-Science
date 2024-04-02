import sys
sys.stdin = open('1860.txt', 'r')

result_1 = []
for _ in range(1000):
    result_1.append(input())
print(result_1)
sys.stdin.close()

sys.stdin = open('test.txt', 'r')
result_2 = []
for _ in range(1000):
    result_2.append(input())
print(result_2)
sys.stdin.close()

import numpy as np
print(np.equal(result_1, result_2))