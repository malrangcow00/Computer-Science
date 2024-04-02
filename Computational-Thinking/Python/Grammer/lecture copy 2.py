def check(text):
    stack = []  # 후입선출 (Last-In-First-Out : LIFO)
    for ch in text:
        # '(' 괄호를 만났을 때에는 '(' 삽입(push)
        if ch == '(':
            stack.append('(')
        # ')' 괄호를 만났을 때에는 삭제(pop)
        elif ch == ')':
            if len(stack) == 0:  # 도중에 비어있는 스택에서 삭제(pop)를 진행
                return False
            stack.pop()  # 삭제를 진행했을 때. '(' == ')', '[' == ']', '{' == '}'

    if len(stack) == 0:
        return True
    else:
        return False


# 괄호 검사 성공한 경우는 괄호 검사를 수행 완료한 후에 스택이 비어있는 경우.
#  //      실패한 경우는 검사를 수행하는 도중에 비어있는 스택에서 삭제(pop)를 진행하려 하거나,
#                        괄호 검사를 수행 완료한 후에 스택이 차 있는 경우.
test = '((( )((((( )( )((( )( ))((( ))))))'

if check(test):
    print("성공")
else:
    print("실패")