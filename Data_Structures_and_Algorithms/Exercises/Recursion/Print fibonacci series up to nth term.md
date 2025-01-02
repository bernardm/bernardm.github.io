# Print fibonacci series up to nth term

## Problem analysis

### Example 1

- Input: N = 5
- Output: 0 1 1 2 3 5
- Explanation: 0 1 1 2 3 5 is the fibonacci series up to 5th term.(0 based indexing)

### Example 2

- Input: 6
- Output: 0 1 1 2 3 5 8
- Explanation: 0 1 1 2 3 5 8 is the fibonacci series up to65th term.(0 based indexing)

## Data analysis

- domain: $0 <= n <= 30$
- error case: none
- edge case: none
- base case:
  - 0: return 0
  - 1: return 1

## Algorithm analysis

```python
# Reducer method
# Time Complexity: $O(n)$
def fibonacciReducer(n):
    if n == 0:
        return [0]
    elif n == 1:
        return fibonacci_list
    else:
        return fibonacciReducer(
            n - 1, fibonacci_list + [fibonacci_list[-2] + fibonacci_list[-1]]
        )


# Multi-recursive call method
# Time Complexity: $O(2^n)$
def fibonacciRecursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacciRecursive(n - 2) + fibonacciRecursive(n - 1)


# Trampoline method
def trampoline(f):
    def trampolined_f(*args, **kwargs):
        result = f(*args, **kwargs)
        while callable(result):
            result = result()
        return result

    return trampolined_f


_fibonacciTrampoline_memo = {}


def _fibonacciTrampoline(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:

        def partial():
            result = _fibonacciTrampoline_memo.get(n, None)
            if result is None:
                result = fibonacciTrampoline(n - 2) + fibonacciTrampoline(n - 1)
                _fibonacciTrampoline_memo[n] = result
            return result

        return partial


fibonacciTrampoline = trampoline(_fibonacciTrampoline)


import unittest


class AbstractTestCase(object):
    def test_base_case(self):
        self.assertEqual(self.function(0), 0)
        self.assertEqual(self.function(1), 1)

    def test_sample(self):
        self.assertEqual(self.function(2), 1)
        self.assertEqual(self.function(3), 2)
        self.assertEqual(self.function(4), 3)
        self.assertEqual(self.function(5), 5)
        self.assertEqual(self.function(6), 8)


class Test_fibonacciRecursive(AbstractTestCase, unittest.TestCase):
    def function(self, param):
        return fibonacciRecursive(param)


class Test_fibonacciTrampoline(AbstractTestCase, unittest.TestCase):
    def function(self, param):
        return fibonacciTrampoline(param)

    def test_domain_upper(self):
        self.assertEqual(self.function(30), 832040)
        self.assertEqual(
            self.function(300),
            222232244629420445529739893461909967206666939096499764990979600,
        )


unittest.main()
```
