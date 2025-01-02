# Reverse an array

You are given an array of integers arr[]. Your task is to reverse the given array.

## Problem analysis

### Example 1

- Input: arr = [1, 4, 3, 2, 6, 5]
- Output: [5, 6, 2, 3, 4, 1]
- Explanation: The elements of the array are 1 4 3 2 6 5. After reversing the array, the first element goes to the last position, the second element goes to the second last position and so on. Hence, the answer is 5 6 2 3 4 1.

### Example 2

- Input: arr = [4, 5, 2]
- Output: [2, 5, 4]
- Explanation: The elements of the array are 4 5 2. The reversed array will be 2 5 4.

### Example 3

- Input: arr = [1]
- Output: [1]
- Explanation: The array has only single element, hence the reversed array is same as the original.

## Data analysis

- domain: $1<=arr.size()<=10^5$ and $0<=arr[i]<=10^5$
- error case: none
- edge case:

  - []: return []

- terminating condition:

  - arr = [1]

- variables:
  - begin_ix
  - end_ix

## Algorithm analysis

### optimized code

```python
def trampoline(f):
    def trampolined_f(*args, **kwargs):
        result = f(*args, **kwargs)
        while callable(result):
            result = result()
        return result

    return trampolined_f


def reverseArray(array):
    reverseArrayTrampoline = trampoline(reverseArrayRecursive)
    return reverseArrayTrampoline(array, 0, len(array) - 1)


def reverseArrayRecursive(array, begin_ix, end_ix):
    if begin_ix < end_ix:
        array[begin_ix], array[end_ix] = array[end_ix], array[begin_ix]
        return lambda: reverseArrayRecursive(array, begin_ix + 1, end_ix - 1)
    else:
        return array


import unittest


class TestFunction(unittest.TestCase):
    def test_domain_lower(self):
        self.assertEqual(reverseArray([1]), [1])

    def test_domain_upper(self):
        arr = list(range(10**5))
        arr_reversed = list(arr[::-1])
        self.assertEqual(reverseArray(arr), arr_reversed)

    def test_edge_case(self):
        self.assertEqual(reverseArray([]), [])

    def test_even_list(self):
        arr = [1, 4, 3, 2, 6, 5]
        arr_reversed = list(arr[::-1])
        self.assertEqual(reverseArray(arr), arr_reversed)

    def test_odd_list(self):
        arr = [0, 1, 2]
        arr_reversed = list(arr[::-1])
        self.assertEqual(reverseArray(arr), arr_reversed)


if __name__ == "__main__":
    unittest.main()
```
