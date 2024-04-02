import sys
input = sys.stdin.readline
T = int(input())
for tc in range(T):
    PS = input().rstrip()
    state = True
    while state:
        if '()' in PS:
            PS = PS.replace('()', '')
        elif PS:
            state = False
            print('NO')
        else:
            state = False
            print('YES')

#     PS = list(input().rstrip())
#     stack = []
#     while PS:
#         tmp = PS.pop()
#         if tmp == ')':
#             stack.append(tmp)
#         else:
#             if stack and stack[-1] == ')':
#                 stack.pop()
#                 Done = True
#             else:
#                 Done = False
#                 break
#
#     if Done and stack == []:
#         print('YES')
#     else:
#         print('NO')
