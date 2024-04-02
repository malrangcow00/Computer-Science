queue_1 = [4, 5, 6]
queue_1.insert(0, 3) # index, value
queue_1.insert(0, 2)
print(queue_1)

print(queue_1.pop(0))
print(queue_1.pop())
print(queue_1)
print()
# deque : double-ended queue
# 양방향에서 추가하고 제거할 수 있는 자료구조
# 첫 번째 데이터를 추가/제거하는 appendleft()/popleft() 메서드 제공

from collections import deque

queue_2 = deque([4, 5, 6])
queue_2.append(7)
queue_2.append(8)
print(queue_2)

print(queue_2.popleft())
print(queue_2.popleft())
print(queue_2)

queue_3 = deque([4, 5, 6])
queue_3.appendleft(3)
queue_3.appendleft(2)
print(queue_3)
print()

# deque의 popleft()와 appendleft(x)메서드는 모두 O(1): 상수의 시간 복잡도를 가지기 때문에, 위에서 살펴본 list의 pop(0)와 insert(0, x) 대비 성능 상에 큰 이점이 있습니다.
#
# 하지만 모든 자료 구조가 그러하듯 deque도 단점이 있습니다. 바로 무작위 접근(random access)의 시간 복잡도가 O(n)이라는 것입니다. 내부적으로 linked list를 사용하고 있기 때문에 i 번째 데이터에 접근하려면 맨 앞/뒤부터 i 번 순회(iteration)가 필요

# Queue
# 파이썬에서 큐를 사용하는 마지막 방법은 queue 모듈의 Queue 클래스를 사용하는 것입니다. 이 방법은 주로 멀티 쓰레딩(threading) 환경에서 사용되며, 내부적으로 라킹(locking)을 지원하여 여러 개의 쓰레드가 동시에 데이터를 추가하거나 삭제할 수 있습니다.

# list나 deque와 달리 방향성이 없기 때문에 데이터 추가와 삭제가 하나의 메서드로 처리됩니다. 따라서, 데이터가 추가하려면 put(x) 메서드를 사용하고, 데이터를 삭제하려면 get() 메서드를 사용합니다.

from queue import Queue

queue_4 = Queue()
queue_4.put(4)
queue_4.put(5)
queue_4.put(6)
print(queue_4)
print(queue_4.get())
print(queue_4.get())
print(queue_4.get())
print(queue_4)

# Queue는 deque처럼 O(1) 데이터 추가/삭제 성능을 보이는데요. list나 deque와 달리 인덱스로 데이터 접근하는 것을 기본적으로는 지원하지 않으니 참고 바라겠습니다.