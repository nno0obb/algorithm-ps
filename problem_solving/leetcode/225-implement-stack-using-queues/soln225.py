"""
# 리트코드
# No. 225 / implement-stack-using-queues
# Python 3.x.y
# by "nno0obb"
"""

from collections import deque


class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int | None:
        if not self.q1:
            self.q1, self.q2 = self.q2, self.q1
        if not self.q1:
            return None
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        return self.q1.popleft()

    def top(self) -> int | None:
        if not self.q1:
            self.q1, self.q2 = self.q2, self.q1
        if not self.q1:
            return None
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        return self.q1[0]

    def empty(self) -> bool:
        return not self.q1 and not self.q2


def test_solution(subtests):
    with subtests.test("Example 1"):
        stack = MyStack()
        stack.push(1)
        stack.push(2)
        assert stack.top() == 2
        assert stack.pop() == 2
        assert stack.empty() is False
    with subtests.test("Example 2"):
        stack = MyStack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        print(stack.q1, stack.q2)
        assert stack.pop() == 3
        print(stack.q1, stack.q2)
        assert stack.pop() == 2
        print(stack.q1, stack.q2)
        assert stack.pop() == 1
        print(stack.q1, stack.q2)
        assert stack.empty() is True
