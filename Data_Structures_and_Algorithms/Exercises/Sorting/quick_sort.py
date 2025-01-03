import unittest
from test_sort import AbstractTestCase
from trampoline import trampoline


def partitionArray(arr, left_ix, right_ix):
    if left_ix < right_ix:
        pivot_ix, pivot_value = right_ix, arr[right_ix]

        while True:
            while arr[left_ix] < pivot_value:
                left_ix += 1

            while left_ix <= right_ix and arr[right_ix] >= pivot_value:
                right_ix -= 1

            if left_ix >= right_ix:
                if left_ix != pivot_ix:
                    arr[left_ix], arr[pivot_ix] = arr[pivot_ix], arr[left_ix]

                # bounds have crossed. end partitioning process
                break
            else:
                # move left, right pair into correct partition
                arr[left_ix], arr[right_ix] = arr[right_ix], arr[left_ix]

    return left_ix


def quickSort(arr: list[int], arr_begin=0, arr_end=None) -> list[int]:
    if arr_end is None:
        arr_end = len(arr) - 1

    if arr_begin < arr_end:
        pivot_ix = partitionArray(arr, arr_begin, arr_end)

        left_begin, left_end = arr_begin, pivot_ix - 1
        right_begin, right_end = pivot_ix + 1, arr_end

        quickSort(arr, left_begin, left_end)
        quickSort(arr, right_begin, right_end)
    return arr


class TestRecursive(AbstractTestCase, unittest.TestCase):
    def function(self, param):
        return quickSort(param)


unittest.main()
