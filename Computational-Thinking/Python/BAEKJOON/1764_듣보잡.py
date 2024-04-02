import sys
N, M = map(int, sys.stdin.readline().split())
set_N = set()
for _ in range(N):
    set_N.add(sys.stdin.readline().rstrip())

set_M = set()
for _ in range(M):
    set_M.add(sys.stdin.readline().rstrip())

print(len(set_N & set_M))
unknown = list(set_N & set_M)
unknown.sort()
for _ in unknown:
    print(_)

# 시간 초과
# import sys
# N, M = map(int, sys.stdin.readline().split())
# nv_heard = {}
# nv_seen = {}
#
# # 사전 찾기
# for _ in range(N):
#     name = sys.stdin.readline().rstrip()
#     if name[0] in nv_heard:
#         nv_heard[name[0]].append(name)
#     else:
#         nv_heard[name[0]] = [name]
#
# # 정렬 필요 x
# # nv_heard = dict(sorted(nv_heard.items()))
#
# cnt = 0
# unknown = []
# for _ in range(M):
#     name = sys.stdin.readline().rstrip()
#     if name in nv_heard[name[0]]:
#         cnt += 1
#         unknown.append(name)
#
# print(cnt)
# for _ in unknown:
#     print(_)