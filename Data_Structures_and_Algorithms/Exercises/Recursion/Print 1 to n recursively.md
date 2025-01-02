# Print 1 to n recursively

This is a function problem. You only need to complete the function printNos() that takes N as parameter and prints number from 1 to N recursively. Don't print newline, it will be added by the driver code.

## Problem analysis

### Example

- Input: N = 10
- Output: 1 2 3 4 5 6 7 8 9 10

## Data analysis

- domain $1 <= n <= 1000$
- error case: none
- edge case: none

## Algorithm analysis

- Time Complexity: $O(n)$
- Space Complexity: $O(n)$

```python
class Solution:
    def printNos(self, n):
        print(" ".join(map(str, self.listAscendingN(n))), end=" ")

    def listAscendingN(self, n):
        if n == 1:
            return [n]
        else:
            return self.listAscendingN(n - 1) + [n]


import unittest


class TestFunction(unittest.TestCase):
    s = Solution()

    def test_base_case(self):
        self.assertEqual(self.s.listAscendingN(1), [1])

    def test_example(self):
        self.assertEqual(self.s.listAscendingN(5), [1, 2, 3, 4, 5])
        self.assertEqual(self.s.listAscendingN(10), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


unittest.main()
```
