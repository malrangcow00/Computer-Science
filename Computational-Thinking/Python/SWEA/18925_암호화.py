import sys, os, re
path = os.path.basename(__file__)
problem_number = re.compile('^([0-9]{4,})').match(path).group(1)
sys.stdin = open(f'input/{problem_number}.txt', 'r')

for t in range(1, int(input())+1):
    n,p,k = int(input()),input(),int(input(),16)
    print(f'#{t} {"".join([hex(int(p[i], 16)^k)[2:].capitalize() for i in range(n)])}')

# for tc in range(1, int(input())+1):
#     input()
#     code = input()
#     key = input()
#     print(f'#{tc} {"".join([hex(int(i, 16)^int(key, 16))[2:].capitalize() for i in code])}')

# for tc in range(1, int(input())+1):
#     input()
#     code = input()
#     key = input()
#     result = ''
#     for i in code:
#         result += hex(int(i, 16)^int(key, 16))[2:].capitalize()
#     print(f'#{tc} {result}')

# decode = {
#     0: '0',
#     1: '1',
#     2: '2',
#     3: '3',
#     4: '4',
#     5: '5',
#     6: '6',
#     7: '7',
#     8: '8',
#     9: '9',
#     10: 'A',
#     11: 'B',
#     12: 'C',
#     13: 'D',
#     14: 'E',
#     15: 'F'
#     }
# 
# for tc in range(1, int(input())+1):
#     input()
#     code = input()
#     key = input()
#     result = ''
#     for i in code:
#         result += decode[int(i, 16)^int(key, 16)]
#     print(f'#{tc}', result)



# # 내장함수 replace 사용금지
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     code = input()
#     key = input()
#     result = []
#     
#     for i in code:
#         result.append(hex(int(i, 16)^int(key, 16))[2:])
#     
#     result = ''.join(result).replace('a', 'A').replace('b', 'B').replace('c', 'C').replace('d', 'D').replace('e', 'E').replace('f', 'F')
#     print(f'#{tc}', result)

