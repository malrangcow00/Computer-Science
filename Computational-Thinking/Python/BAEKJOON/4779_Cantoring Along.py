import sys
input = sys.stdin.readline

# 칸토어 집합
def The_Cantor_set(string):
    if len(string) == 1:
        return string
    left = The_Cantor_set(string[:len(string)//3])
    mid = ' ' * (len(string)//3)
    right = The_Cantor_set(string[2*len(string)//3:])
    return left + mid + right

while True:
    try:
        N = int(input())
        string = '-' * 3**N
        print(The_Cantor_set(string))
    except:
        break