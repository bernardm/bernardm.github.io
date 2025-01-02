# Print n to 1 recursively

This is a function problem. You only need to complete the function printNos() that takes N as parameter and prints number from N to 1 recursively. Don't print newline, it will be added by the driver code.

## Problem analysis

### Example

- Input: N = 10
- Output: 10 9 8 7 6 5 4 3 2 1

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
        if n == 1:
            print(n, end=" ")
            return [1]
        else:
            print(n, end=" ")
            return [n] + self.printNos(n - 1)


import unittest


class TestFunction(unittest.TestCase):
    s = Solution()

    def test_base_case(self):
        self.assertEqual(self.s.printNos(1), [1])

    def test_example(self):
        self.assertEqual(self.s.printNos(10), [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])


unittest.main()
```
