import sys
sys.stdin = open('input/4866.txt', 'r')

T = int(input())

open_list = ['[', '{', '(']
close_list = [']', '}', ')']

small = False
large = False

for tc in range(1, T+1):
    stack = []
    check_list = input()
    result = 1
    for i in check_list:
        if small == True:
            if i == "'":
                small = False
                continue
        if large == True:
            if i == '"':
                large = False
                continue
        if i == "'":
            small = True
            continue
        if i == '"':
            large = True
            continue
        if small == False and large == False:
            if i in open_list:
                stack.append(i)
            elif i in close_list:
                if len(stack) == 0 or open_list.index(stack.pop()) != close_list.index(i):
                    result = 0
                    break
                
    if len(stack) != 0:
        result = 0
    
    print(f'#{tc} {result}')