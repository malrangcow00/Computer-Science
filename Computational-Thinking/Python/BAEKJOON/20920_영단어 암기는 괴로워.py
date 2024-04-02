import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dictionary = {}
for _ in range(N):
    word = input().rstrip()
    if len(word) < M:
        continue
    else:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1

dictionary = dict(sorted(dictionary.items(), key = lambda x : (-x[1], -len(x[0]), x[0])))

for _ in dictionary.keys():
    print(_)