import sys
input = sys.stdin.readline

Q = int(input())
query = []
for i in range(31):
    query.append(2**i)
for _ in range(Q):
    a = int(input())
    if a in query:
        print(1)
    else:
        print(0)