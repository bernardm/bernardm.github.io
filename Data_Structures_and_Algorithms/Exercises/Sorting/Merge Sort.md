# Merge Sort Algorithm

Given an array of size n, sort the array using **Merge Sort**. The problem needs to be broken down into sub problems. `mergeArray()` and `mergeSort()`

## mergeArray()

### Problem analysis

#### Example 1

- Input: [1, 2, 5, 6], [3, 4, 7, 8]
- Output: [1, 2, 3, 4, 5, 6, 7, 8]

#### Example 2

- Input: [1, 2, 3], [4]
- Output: [1, 2, 3, 4]

### Data analysis

- domain:

  - $1 <= arr.size() <= 10^5$
  - $1 <= arr[i] <= 10^5$

- error case: none
- edge case:
  - [], []: []
  - [], [1]: [1]
  - [1], []: [1]
  - [2], [1]: [1, 2]

## mergeSort()

### Problem analysis

#### Example 1

- Input: N=5, arr[]=[4,2,1,6,7]
- Output: 1,2,4,6,7,

#### Example 2

- Input: N=7,arr[]=[3,2,8,5,1,4,23]
- Output: 1,2,3,4,5,8,23

### Data analysis

- domain:

  - $1 <= arr.size() <= 10^5$
  - $1 <= arr[i] <= 10^5$

- error case: none
- edge case:
  - []: return []
  - [1]: return [1]
  - [2,1]: return [1,2]
- variables:

## Code

```python
def mergeArray(left_array: list[int] = [], right_array: list[int] = []) -> list[int]:
    """
    Merges given arrays in ascending order, returning a new array.

    Time complexity: O(n)

    Args:
        left_array (list[int]): The first array to merge.
        right_array (list[int]): The second array to merge.

    Returns:
        list[int]: New array. Merged in ascending order.
    """

    left_ix, left_len = 0, len(left_array)
    right_ix, right_len = 0, len(right_array)
    merged_array: list[int] = []

    if left_len == 0:
        return list(right_array)
    elif right_len == 0:
        return list(left_array)

    while True:
        if left_array[left_ix] < right_array[right_ix]:
            merged_array.append(left_array[left_ix])
            left_ix += 1
            if left_ix == left_len:
                merged_array.extend(right_array[right_ix:])
                break
        else:
            merged_array.append(right_array[right_ix])
            right_ix += 1
            if right_ix == right_len:
                merged_array.extend(left_array[left_ix:])
                break

    return merged_array


def mergeSort(input_array: list[int]) -> list[int]:
    """
    Sorts the given array in ascending order, using the merge sort algorithm, and returns a new array.

    Time complexity: O(n log n)

    Args:
        input_array (list[int]): The array to sort.

    Returns:
        list[int]: New array. Sorted in ascending order.
    """

    input_len = len(input_array)

    if input_len <= 1:
        return list(input_array)
    elif input_len == 2:
        a, b = input_array
        return [a, b] if a < b else [b, a]
    else:
        midpoint = input_len // 2
        return mergeArray(
            mergeSort(input_array[:midpoint]),
            mergeSort(input_array[midpoint:]),
        )


import unittest
import random


class Test_mergeSort(unittest.TestCase):
    def test_edge_case_empty(self):
        self.assertEqual(mergeSort([]), [])

    def test_edge_case_single_element(self):
        self.assertEqual(mergeSort([1]), [1])

    def test_edge_case_two_elements(self):
        self.assertEqual(mergeSort([2, 1]), [1, 2])

    def test_sort_ascending(self):
        self.assertEqual(mergeSort([2, 1, 3, 5, 4]), [1, 2, 3, 4, 5])

    def test_domain_upper(self):
        unsorted = list(range(10**5))
        random.shuffle(unsorted)
        self.assertEqual(mergeSort(unsorted)[:10], list(range(10)))


class Test_mergeArray(unittest.TestCase):
    def test_edge_case_both_empty(self):
        self.assertEqual(mergeArray([], []), [])

    def test_edge_case_left_empty(self):
        self.assertEqual(mergeArray([], [1]), [1])

    def test_edge_case_right_empty(self):
        self.assertEqual(mergeArray([1], []), [1])

    def test_edge_case_one_element(self):
        self.assertEqual(mergeArray([2], [1]), [1, 2])

    def test_merge_equal_length(self):
        self.assertEqual(
            mergeArray([1, 2, 5, 6], [3, 4, 7, 8]), [1, 2, 3, 4, 5, 6, 7, 8]
        )

    def test_merge_unequal_length(self):
        self.assertEqual(mergeArray([1, 2, 5, 6], [3, 4]), [1, 2, 3, 4, 5, 6])


unittest.main()
```
