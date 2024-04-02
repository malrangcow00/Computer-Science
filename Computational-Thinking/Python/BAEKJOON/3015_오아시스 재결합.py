import sys
input = sys.stdin.readline

N = int(input())
line = []
for _ in range(N):
    line.append(int(input()))
    
cnt = 0
stack = []
for i in line:
    while stack and stack[-1][0] < i:
        cnt += stack.pop()[1]
    if not stack:
        stack.append((i, 1))
        continue
    if stack[-1][0] == i:
        cnt = stack.pop()[1]
        cnt += cnt
        if stack:
            cnt += 1
            stack.append((i, cnt + 1))
    else:
        stack.append((i, 1))
        cnt += 1
print(cnt)

# ------------

# cnt = i = 0
# j = 1
# k = 0
# while i < N:
#     while j < N:
#         # a가 b보다 같거나 크고 둘 사이에 높은 곳이 없음
#         # 카운트를 추가하고 k를 갱신하면서 계속해서 먼거리를 탐색
#         if line[i] >= line[j] >= k:
#             k = max(k, line[j])
#             cnt += 1
#             j += 1
#         # a가 b보다 작다 -> 다음 거리를 탐색할수가없다 -> i를 증가
#         # 둘사이에 높은 곳이 없기 때문에 카운트를 추가하고 k를 초기화
#         elif k <= line[i] < line[j]:
#             i += 1
#             j = i+1
#             cnt += 1
#             k = 0
#         # a가 b보다 작거나 둘 사이에 더 높은 곳이 있다
#         # 카운트를 하지 않고 k를 갱신하면서 더 먼 거리를 탐색
#         else:
#             k = max(k, line[j])
#             j += 1
#     i += 1
#     j = i+1
#     k = 0
# print(cnt)
