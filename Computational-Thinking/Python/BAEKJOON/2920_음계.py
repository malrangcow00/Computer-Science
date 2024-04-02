import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))
ascending = list(range(1, 9))
decending = list(range(8, 0, -1))

if arr == ascending:
    print('ascending')
elif arr == decending:
    print('descending')
else:
    print('mixed')