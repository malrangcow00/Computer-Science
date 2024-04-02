tri = list(map(int, input().split()))
if 2*max(tri) >= sum(tri):
    print(2*sum(tri) - 2*max(tri) -1)
else:
    print(sum(tri))