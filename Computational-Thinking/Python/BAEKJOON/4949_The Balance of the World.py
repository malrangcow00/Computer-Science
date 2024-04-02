import sys
input = sys.stdin.readline
PS = ['(', ')', '[', ']']
while True:
    sen = input().rstrip()
    if sen == '.':
        break
    string = ''
    for _ in sen:
        if _ in PS:
            string += _
    while True:
        if '()' in string:
            string = string.replace('()', '')
        elif '[]' in string:
            string = string.replace('[]', '')
        elif string:
            print('no')
            break
        else:
            print('yes')
            break