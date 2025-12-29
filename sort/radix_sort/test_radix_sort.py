import random
from itertools import chain

import pytest

MAX_ARR_LEN = 10_000
MAX_VAL = 10_000
ITERATIONS = 2
ROUNDS = 2


def radix_sort(arr: list[int]) -> list[int]:
    max_digits = max(map(lambda x: len(str(abs(x))), arr))
    plus_buckets = [[[] for _ in range(10)] for _ in range(max_digits + 1)]
    minus_buckets = [[[] for _ in range(10)] for _ in range(max_digits + 1)]

    for num in arr:
        if num >= 0:
            plus_buckets[0][0].append((num, num))
        elif num < 0:
            minus_buckets[0][0].append((num, num))

    for i in range(1, max_digits + 1):
        for plus_bucket in plus_buckets[i - 1]:
            for res, num in plus_bucket:
                plus_buckets[i][res % 10].append((res // 10, num))
        for minus_bucket in minus_buckets[i - 1]:
            for res, num in minus_bucket:
                minus_buckets[i][res % 10].append((res // 10, num))

    arr = [num for _, num in chain.from_iterable(minus_buckets[max_digits] + plus_buckets[max_digits])]
    return arr


@pytest.fixture(name="create_random_arr")
def _create_random_arr():
    global MAX_VAL

    def _make(arr_len: int) -> list[int]:
        return [random.randint(-MAX_VAL, MAX_VAL) for _ in range(arr_len)]

    return _make


def test_radix_sort(benchmark, create_random_arr):
    global MAX_ARR_LEN, ITERATIONS, ROUNDS

    random_arr = create_random_arr(MAX_ARR_LEN)
    benchmark.pedantic(
        radix_sort,
        args=(random_arr,),
        iterations=ITERATIONS,
        rounds=ROUNDS,
    )
    assert sorted(random_arr) == radix_sort(random_arr)
