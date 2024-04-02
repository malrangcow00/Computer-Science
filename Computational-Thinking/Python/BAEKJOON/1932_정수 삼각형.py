import sys
input = sys.stdin.readline

N = int(input())
triangle = []
for _ in range(N):
    triangle.append(list(map(int, input().split())))


for y in range(1, N):
    for x in range(y+1):
        if x == 0:
            triangle[y][x] = triangle[y][x] + triangle[y-1][x]
        elif x == y:
            triangle[y][x] = triangle[y][x] + triangle[y-1][x-1]
        else:
            triangle[y][x] = triangle[y][x] + max(triangle[y-1][x], triangle[y-1][x-1])

print(max(triangle[N-1]))


# 재귀 시간초과

# total = triangle[0][0]
#
# def plus(total, i, depth):
#     global mx
#     if depth == N:
#         mx = max(mx, total)
#     else:
#         total += triangle[depth][i]
#         plus(total, i, depth+1)
#         total += triangle[depth][i+1] - triangle[depth][i]
#         plus(total, i+1, depth+1)
#
# mx = 0
# plus(total, 0, 1)
#
# print(mx)