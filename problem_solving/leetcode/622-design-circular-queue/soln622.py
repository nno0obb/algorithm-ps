"""
# 리트코드
# No. 622 / design-circular-queue
# Python 3.x.y
# by "nno0obb"
"""

from collections import deque


class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = deque(maxlen=k)

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue.append(value)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.queue.popleft()
        return True

    def Front(self) -> int:
        return self.queue[0] if self.queue else -1

    def Rear(self) -> int:
        return self.queue[-1] if self.queue else -1

    def isEmpty(self) -> bool:
        return len(self.queue) == 0

    def isFull(self) -> bool:
        return len(self.queue) == self.queue.maxlen


def test_solution(subtests):
    with subtests.test("Example 1"):
        circular_queue = MyCircularQueue(3)
        assert circular_queue.enQueue(1) is True
        assert circular_queue.enQueue(2) is True
        assert circular_queue.enQueue(3) is True
        assert circular_queue.enQueue(4) is False
        assert circular_queue.Rear() == 3
        assert circular_queue.isFull() is True
        assert circular_queue.deQueue() is True
        assert circular_queue.enQueue(4) is True
        assert circular_queue.Rear() == 4
