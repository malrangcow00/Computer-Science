import sys
T = int(sys.stdin.readline())
for tc in range(T):
    A, B = map(int, sys.stdin.readline().split())
    a, b, c = A, B, A % B
    # 유클리드 호제법
    while c != 0:
        a = b
        b = c
        c = a % b
    # b: 최소공약수
    print(A//b*B)