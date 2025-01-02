# Print name n times using recursion

## Problem analysis

## Example

- Input: 5
- Output: GFG GFG GFG GFG GFG

## Data analysis

- domain: $1 <= n <= 1000$
- error: none
- edge:
  n = 0: ""

## Algorithm analysis

### brute force solution

Time Complexity: $O(n)$

```python
class Solution:
    def printGfg(self, n):
        if n == 0:
            return ""
        else:
            print("GFG", end=" ")
            return "GFG " + self.printGfg(n - 1)


import unittest


class TestPrintGfg(unittest.TestCase):
    s = Solution()

    def test_edge(self):
        self.assertEqual(self.s.printGfg(0), "")

    def test_example(self):
        self.assertEqual(self.s.printGfg(5), "GFG GFG GFG GFG GFG ")


unittest.main()
```
