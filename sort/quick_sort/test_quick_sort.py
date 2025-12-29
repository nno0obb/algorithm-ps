import random

import pytest

MAX_ARR_LEN = 10_000
MAX_VAL = 10_000
ITERATIONS = 2
ROUNDS = 2


def quick_sort(arr: list[int]) -> list[int]:

    def _quick_sort(ldx: int, rdx: int) -> None:
        if ldx >= rdx:
            return

        mdx = (ldx + rdx) // 2
        pivot = arr[mdx]

        idx, jdx = ldx, rdx
        while idx <= jdx:
            while arr[idx] < pivot:
                idx += 1
            while arr[jdx] > pivot:
                jdx -= 1
            if idx <= jdx:
                arr[idx], arr[jdx] = arr[jdx], arr[idx]  # Swap
                idx += 1
                jdx -= 1

        _quick_sort(ldx, idx - 1)
        _quick_sort(idx, rdx)

    _quick_sort(0, len(arr) - 1)
    return arr


@pytest.fixture(name="create_random_arr")
def _create_random_arr():
    global MAX_VAL

    def _make(arr_len: int) -> list[int]:
        return [random.randint(-MAX_VAL, MAX_VAL) for _ in range(arr_len)]

    return _make


def test_quick_sort(benchmark, create_random_arr):
    global MAX_ARR_LEN, ITERATIONS, ROUNDS

    random_arr = create_random_arr(MAX_ARR_LEN)
    benchmark.pedantic(
        quick_sort,
        args=(random_arr,),
        iterations=ITERATIONS,
        rounds=ROUNDS,
    )
    assert sorted(random_arr) == quick_sort(random_arr)
