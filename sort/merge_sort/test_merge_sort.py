import random

import pytest

MAX_ARR_LEN = 10_000
MAX_VAL = 10_000
ITERATIONS = 2
ROUNDS = 2


def merge_sort(arr: list[int]) -> list[int]:
    tmp = [-1] * len(arr)

    def _merge_sort(ldx: int, rdx: int) -> None:
        if ldx >= rdx:
            return

        mdx = (ldx + rdx) // 2
        _merge_sort(ldx, mdx)
        _merge_sort(mdx + 1, rdx)

        for i in range(ldx, rdx + 1):
            tmp[i] = arr[i]

        idx, jdx, kdx = ldx, mdx + 1, ldx
        while idx <= mdx and jdx <= rdx:
            if tmp[idx] > tmp[jdx]:
                arr[kdx] = tmp[jdx]
                jdx += 1
                kdx += 1
            elif tmp[idx] <= tmp[jdx]:
                arr[kdx] = tmp[idx]
                idx += 1
                kdx += 1

        while idx <= mdx:
            arr[kdx] = tmp[idx]
            idx += 1
            kdx += 1

        while jdx <= rdx:
            arr[kdx] = tmp[jdx]
            jdx += 1
            kdx += 1

    _merge_sort(0, len(arr) - 1)
    return arr


@pytest.fixture(name="create_random_arr")
def _create_random_arr():
    global MAX_VAL

    def _make(arr_len: int) -> list[int]:
        return [random.randint(-MAX_VAL, MAX_VAL) for _ in range(arr_len)]

    return _make


def test_merge_sort(benchmark, create_random_arr):
    global MAX_ARR_LEN, ITERATIONS, ROUNDS

    random_arr = create_random_arr(MAX_ARR_LEN)
    benchmark.pedantic(
        merge_sort,
        args=(random_arr,),
        iterations=ITERATIONS,
        rounds=ROUNDS,
    )
    assert sorted(random_arr) == merge_sort(random_arr)
