import sys
input = sys.stdin.readline

N = int(input())
dance_with = {'ChongChong'}

for _ in range(N):
    dancer_1, dancer_2 = input().split()

    if dancer_1 in dance_with:
        dance_with.add(dancer_2)

    if dancer_2 in dance_with:
        dance_with.add(dancer_1)

print(len(dance_with))