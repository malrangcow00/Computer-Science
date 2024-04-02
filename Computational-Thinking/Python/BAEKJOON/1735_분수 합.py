import sys
arr = [*sys.stdin.readline().split(), *sys.stdin.readline().split()]
A, B = int(arr[0]) * int(arr[3]) + int(arr[1]) * int(arr[2]), int(arr[1]) * int(arr[3])
a, b, c = A, B, A % B
while c != 0:
    a = b
    b = c
    c = a % b
print(A//b, B//b)