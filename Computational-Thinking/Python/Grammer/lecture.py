# 빈 리스트
stack = []


# push : 마지막의 요소를 삽입
def push(item):
    stack.append(item)


# isEmpty : 현재 스택이 비어있는지 여부를 반환해주는 함수
def isEmpty():
    return len(stack) == 0

# pop :  마지막의 요소를 꺼내는 연산
# pop을 시행했을 때 요소가 없다면??? (에러!)
def pop():
    if isEmpty():
        return
    return stack.pop()


# peek : 가장 마지막에 넣었던 요소의 값을 반환 함수
def peek():
    if isEmpty():
        return
    return stack[-1]


# 삽입(push) 3개
push(10)
push(20)
push(30)

# 삭제(pop) 3개
item = pop()
print(item)  # 30
item = pop()
print(item)  # 20
item = pop()
print(item)  # 10