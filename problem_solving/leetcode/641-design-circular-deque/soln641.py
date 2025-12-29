"""
# 리트코드
# No. 641 / design-circular-deque
# Python 3.x.y
# by "nno0obb"
"""

from collections import deque


class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = deque(maxlen=k)

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.deque.appendleft(value)
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.deque.append(value)
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.deque.popleft()
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.deque.pop()
        return True

    def getFront(self) -> int:
        return self.deque[0] if self.deque else -1

    def getRear(self) -> int:
        return self.deque[-1] if self.deque else -1

    def isEmpty(self) -> bool:
        return len(self.deque) == 0

    def isFull(self) -> bool:
        return len(self.deque) == self.deque.maxlen


def test_solution(subtests):
    with subtests.test("Example 1"):
        circular_deque = MyCircularDeque(3)
        assert circular_deque.insertLast(1) is True
        assert circular_deque.insertLast(2) is True
        assert circular_deque.insertFront(3) is True
        assert circular_deque.insertFront(4) is False
        assert circular_deque.getRear() == 2
        assert circular_deque.isFull() is True
        assert circular_deque.deleteLast() is True
        assert circular_deque.insertFront(4) is True
        assert circular_deque.getFront() == 4
