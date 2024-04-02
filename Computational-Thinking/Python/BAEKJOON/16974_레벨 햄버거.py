import sys
input = sys.stdin.readline

layer = [1] * 51
patty = [1] * 51

for i in range(1, N+1)
    layer[i] = layer[i-1] * 2 + 3
    patty[i] = patty[i-1] * 2 + 1
    
    if
        
    elif
    
    elif
    
    elif
    
# # 2차 시도
# import sys
# input = sys.stdin.readline
# 
# def dp(N):
#     if N == 0:
#         return [1]
#     return [0] + dp(N-1) + [1] + dp(N-1) +[0]
# 
# N, X = map(int, input().split())
# print(sum(dp(N)[-X:]))

# # 1차 시도
# import sys
# input = sys.stdin.readline
# 
# def dp(N):
#     if N == 0:
#         return 'P'
#     return 'B'+dp(N-1)+'P'+dp(N-1)+'B'
# 
# N, X = map(int, input().split())
# print(dp(N)[-X:].count('P'))