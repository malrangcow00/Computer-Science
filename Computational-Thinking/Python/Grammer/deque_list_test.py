# deque(데크, Double End Queue)
from collections import deque

dq = deque()
# 인큐 (삽입) 1,2,3
dq.append(1)
dq.append(2)
dq.append(3)

# 디큐 (삭제) 1,2,3
item = dq.popleft()
print(item)
item = dq.popleft()
print(item)
item = dq.popleft()
print(item)
print()

# 스택 : 후입선출 (LIFO)
stack = deque()

# 스택에 요소를 삽입 (push)
stack.append(1)
stack.append(2)
stack.append(3)


# 요소를 삭제 (pop)
item = stack.pop()
print(item)
item = stack.pop()
print(item)
item = stack.pop()
print(item)