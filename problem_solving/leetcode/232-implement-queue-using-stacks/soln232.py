"""
# 리트코드
# No. 232 / implement-queue-using-stacks
# Python 3.x.y
# by "nno0obb"
"""


class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        while self.s2:
            self.s1.append(self.s2.pop())
        self.s1.append(x)

    def pop(self) -> int | None:
        while self.s1:
            self.s2.append(self.s1.pop())
        if not self.s2:
            return None
        return self.s2.pop()

    def peek(self) -> int | None:
        while self.s1:
            self.s2.append(self.s1.pop())
        if not self.s2:
            return None
        return self.s2[-1]

    def empty(self) -> bool:
        return not self.s1 and not self.s2


def test_solution(subtests):
    with subtests.test("Example 1"):
        queue = MyQueue()
        queue.push(1)
        queue.push(2)
        assert queue.peek() == 1
        assert queue.pop() == 1
        assert queue.empty() is False
    with subtests.test("Example 2"):
        queue = MyQueue()
        queue.push(1)
        queue.push(2)
        queue.push(3)
        queue.push(4)
        assert queue.pop() == 1
        queue.push(5)
        assert queue.pop() == 2
        assert queue.pop() == 3
        assert queue.pop() == 4
        assert queue.pop() == 5
