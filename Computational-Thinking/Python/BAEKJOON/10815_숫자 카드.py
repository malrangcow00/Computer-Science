import sys

sys.stdin.readline()
arr_N = set(map(int, sys.stdin.readline().split()))
sys.stdin.readline()
for card in map(int, sys.stdin.readline().split()):
    if card in arr_N:
        print(1, end=' ')
    else:
        print(0, end=' ')