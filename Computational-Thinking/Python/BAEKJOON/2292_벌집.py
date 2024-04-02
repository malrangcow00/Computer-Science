total = 0
n = 1
N = int(input())
if N == 1:
    total = 1
    n = 2
while total < N-1:
    total += 6*n-6
    n += 1

print(n-1)
