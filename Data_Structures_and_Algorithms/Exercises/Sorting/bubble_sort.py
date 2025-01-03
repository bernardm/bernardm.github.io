import unittest
from test_sort import AbstractTestCase
from trampoline import trampoline


def bubbleSort(arr: list[int]) -> list[int]:
    """
    Sorts the input list using the bubble sort algorithm.
    Time complexity: O(n^2)


    :param arr: The list to sort.
    :return: The sorted list.
    """

    arr_len = len(arr)

    if arr_len <= 1:
        return arr

    # partition arr as follows: unsorted | sorted
    # call the sweeping action over the remaining unsorted array
    for boundary_len in range(arr_len, 1, -1):
        # sweep the largest element to the end of the array
        for ix in range(1, boundary_len):
            if arr[ix - 1] > arr[ix]:
                arr[ix - 1], arr[ix] = arr[ix], arr[ix - 1]

        # the largest element is now at the end of the array

    return arr


def _bubbleSortRecursive(arr: list[int], partition_len=None) -> list[int]:
    """
    Sorts the input list using the bubble sort algorithm.
    Time complexity: O(n^2)


    :param arr: The list to sort.
    :param partition_len: The length of the unsorted partition.
    :return: The sorted list.
    """
    if partition_len is None:
        partition_len = len(arr)

    # edge cases
    if partition_len <= 1:
        return arr

    # partition arr as follows: unsorted | sorted
    # sweep the largest element to the end of the array
    for ix in range(1, partition_len):
        if arr[ix - 1] > arr[ix]:
            arr[ix - 1], arr[ix] = arr[ix], arr[ix - 1]

    # call the sweeping action over the remaining unsorted array
    return lambda: _bubbleSortRecursive(arr, partition_len - 1)


bubbleSortRecursive = trampoline(_bubbleSortRecursive)


class TestIterative(AbstractTestCase, unittest.TestCase):
    def function(self, param):
        return bubbleSort(param)


class TestRecursive(AbstractTestCase, unittest.TestCase):
    def function(self, param):
        return bubbleSortRecursive(param)


unittest.main()
