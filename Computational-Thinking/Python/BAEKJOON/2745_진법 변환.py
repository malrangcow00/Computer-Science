import sys

N, B = map(str, sys.stdin.readline().split())
N = list(N)
B = int(B)

for i in range(len(N)):
    # 인덱스가 숫자인 경우 변환 X
    # if N[i] not in range(10): # 잘못됨 N[i]가 숫자라도 문자열이므로...
    if not N[i].isdigit():
        N[i] = ord(N[i])-55
    # string 형태의 숫자를 int로 변환
    else:
        N[i] = int(N[i])
    
total = 0

for i in range(1, len(N)+1):
    total += N[-i] * B**(i-1)

print(total)

# Python 내장함수를 이용한 방법
# import sys

# N, B = map(str, sys.stdin.readline().split())
# N = list(N)
# B = int(B)

# total = int(N, int(B))

# print(total)
