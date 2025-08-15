"""
# 리트코드
# No. 706 / design-hashmap
# Python 3.x.y
# by "nno0obb"
"""


class MyHashMap:

    def __init__(self):
        self.dict = {}

    def put(self, key: int, value: int) -> None:
        self.dict[key] = value

    def get(self, key: int) -> int:
        return self.dict.get(key, -1)

    def remove(self, key: int) -> None:
        return self.dict.pop(key, None)


def test_solution(subtests):
    with subtests.test("Example 1"):
        hash_map = MyHashMap()
        hash_map.put(1, 1)
        hash_map.put(2, 2)
        assert hash_map.get(1) == 1
        assert hash_map.get(3) == -1
        hash_map.put(2, 1)
        assert hash_map.get(2) == 1
        hash_map.remove(2)
        assert hash_map.get(2) == -1
