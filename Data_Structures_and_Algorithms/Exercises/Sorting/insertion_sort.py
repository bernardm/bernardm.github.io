import unittest
from test_sort import AbstractTestCase
from trampoline import trampoline


def insertionSort(arr: list[int]) -> list[int]:
    """
    Sorts the input list in place using the insertion sort algorithm.
    Time complexity: O(n^2)

    :param arr: The list to sort.
    :return: The sorted list.
    """
    arr_len = len(arr)

    if arr_len <= 1:
        return arr

    # partition arr as follows: sorted | unsorted
    for boundary_ix in range(1, arr_len):
        # sweep the boundary_value to the left until it is in place
        ix = boundary_ix
        while ix > 0 and arr[ix - 1] > arr[ix]:
            arr[ix - 1], arr[ix] = arr[ix], arr[ix - 1]
            ix -= 1

    return arr


def _insertionSortRecursive(arr: list[int], boundary_ix=1, arr_len=None) -> list[int]:
    """
    Sorts the input list in place using the insertion sort algorithm.
    Time complexity: O(n^2)

    :param arr: The list to sort.
    :param boundary_ix: The index of the boundary between the sorted and unsorted parts of the list.
    :param arr_len: The length of the list.
    :return: The sorted list.
    """
    if arr_len is None:
        arr_len = len(arr)

    if boundary_ix >= arr_len:
        return arr

    # partition the array as follows: sorted | unsorted
    # sweep the unsorted value to the left until it is in place
    ix = boundary_ix
    while ix > 0 and arr[ix - 1] > arr[ix]:
        arr[ix - 1], arr[ix] = arr[ix], arr[ix - 1]
        ix -= 1

    # next unsorted value
    return lambda: _insertionSortRecursive(arr, boundary_ix + 1, arr_len)


insertionSortRecursive = trampoline(_insertionSortRecursive)


class TestIterative(AbstractTestCase, unittest.TestCase):
    def function(self, param):
        return insertionSort(param)


class TestRecursive(AbstractTestCase, unittest.TestCase):
    def function(self, param):
        return insertionSortRecursive(param)


unittest.main()
