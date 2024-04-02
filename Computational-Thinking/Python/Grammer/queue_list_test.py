# 큐... 선입선출(FIFO)
queue = []

# 큐 요소를 추가하는 연산
def enQueue(item):
    queue.append(item)


# 큐 요소를 삭제하는 연산
def deQueue():
    return queue.pop(0)


enQueue(1)
enQueue(2)
enQueue(3)

item = deQueue()
print(item)
item = deQueue()
print(item)
item = deQueue()
print(item)