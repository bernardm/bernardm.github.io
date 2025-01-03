def selectionSort(arr: list[int]) -> list[int]:
    """
    Sorts the input list using the selection sort algorithm.
    Time complexity: O(n^2)

    :param arr: The list to sort.
    :return: The sorted list.
    """

    arr_len = len(arr)

    if arr_len <= 1:
        return arr

    # partition arr as follows: sorted | unsorted
    for boundary_ix in range(arr_len):
        min_ix, min_value = boundary_ix, arr[boundary_ix]

        # find the index of the smallest unsorted number
        for ix in range(boundary_ix + 1, arr_len):
            if arr[ix] < min_value:
                min_ix, min_value = ix, arr[ix]

        # place the min value at the end of the sorted array
        arr[boundary_ix], arr[min_ix] = arr[min_ix], arr[boundary_ix]

    return arr


import unittest
from test_sort import AbstractTestCase


class TestFunction(AbstractTestCase, unittest.TestCase):
    def function(self, param):
        return selectionSort(param)


unittest.main()
