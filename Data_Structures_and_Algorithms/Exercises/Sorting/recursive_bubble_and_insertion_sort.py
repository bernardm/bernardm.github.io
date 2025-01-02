def bubbleSortRecursive(arr):
    arr_len = len(arr)
    return _bubbleSortRecursive(arr, 0, arr_len - 1, arr_len)


def _bubbleSortRecursive(arr, begin_ix, end_ix, boundary_ix):
    if boundary_ix <= 1:
        return arr
    elif boundary_ix == 2:
        if arr[begin_ix] > arr[end_ix]:
            arr[begin_ix], arr[end_ix] = arr[end_ix], arr[begin_ix]
        return arr
    else:
        # sweep all the way to the end of the unsorted list
        for curr_ix in range(begin_ix + 1, boundary_ix):
            if arr[curr_ix - 1] > arr[curr_ix]:
                arr[curr_ix - 1], arr[curr_ix] = arr[curr_ix], arr[curr_ix - 1]

        return _bubbleSortRecursive(arr, 0, end_ix - 1, boundary_ix - 1)


def insertionSortRecursive(arr):
    arr_len = len(arr)
    return _insertionSortRecursive(arr, arr_len - 1, arr_len, arr_len - 2)


def _insertionSortRecursive(arr, begin_ix, end_ix, boundary_ix):
    if boundary_ix < 0:
        return arr

    for cur_ix in range(boundary_ix, end_ix - 1):
        if arr[cur_ix] > arr[cur_ix + 1]:
            arr[cur_ix], arr[cur_ix + 1] = arr[cur_ix + 1], arr[cur_ix]

    return _insertionSortRecursive(arr, begin_ix - 1, end_ix, boundary_ix - 1)


import unittest


class AbstractTestCase(object):
    def test_empty(self):
        self.assertEqual(self.function([]), [])

    def test_1_element(self):
        self.assertEqual(self.function([1]), [1])

    def test_2_elements(self):
        self.assertEqual(self.function([2, 1]), [1, 2])
        self.assertEqual(self.function([1, 2]), [1, 2])

    def test_unsorted_list(self):
        self.assertEqual(self.function([2, 1, 3]), [1, 2, 3])
        self.assertEqual(self.function([2, 3, 1]), [1, 2, 3])
        self.assertEqual(self.function([3, 2, 1]), [1, 2, 3])

    def test_sorted_list(self):
        self.assertEqual(self.function([1, 2, 3]), [1, 2, 3])

    def test_4_elements(self):
        self.assertEqual(self.function([4, 3, 2, 1]), [1, 2, 3, 4])


class Test_bubbleSortRecursive(AbstractTestCase, unittest.TestCase):
    def function(self, param):
        return bubbleSortRecursive(param)


class Test_insertionSortRecursive(AbstractTestCase, unittest.TestCase):
    def function(self, param):
        return insertionSortRecursive(param)


unittest.main()
