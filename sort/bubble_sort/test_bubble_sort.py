import random

import pytest

MAX_ARR_LEN = 10_000
MAX_VAL = 10_000
ITERATIONS = 2
ROUNDS = 2


def bubble_sort(arr: list[int]) -> list[int]:
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap
    return arr


@pytest.fixture(name="create_random_arr")
def _create_random_arr():
    global MAX_VAL

    def _make(arr_len: int) -> list[int]:
        return [random.randint(-MAX_VAL, MAX_VAL) for _ in range(arr_len)]

    return _make


def test_bubble_sort(benchmark, create_random_arr):
    global MAX_ARR_LEN, ITERATIONS, ROUNDS

    random_arr = create_random_arr(MAX_ARR_LEN)
    benchmark.pedantic(
        bubble_sort,
        args=(random_arr,),
        iterations=ITERATIONS,
        rounds=ROUNDS,
    )
    assert sorted(random_arr) == bubble_sort(random_arr)
