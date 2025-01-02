# Factorial of a number

## Problem

### Example 1

- Input: X = 5
- Output: 120
- Explanation: 5! = 5*4*3*2*1

### Example 2

- Input: X = 3
- Output: 6
- Explanation: 3!=3*2*1

## Plan

### domain analysis

- domain:

  - positive integers: 0 < n < infinity

- edge case:

  - negative: abs(n)

- terminal condition:
  - 0: return 1
  - 1: return 1

## Code

### brute force

Time complexity: $O(n)$

```python
def factorial(n: int) -> int:
    if n < 0:    # negative numbers
        return -1 * factorial(abs(n))
    elif n < 1:  # terminal condition
        return 1
    else:        # base case
        return n * factorial(n - 1)


import unittest


class TestFactorial(unittest.TestCase):
    def test_0(self):
        self.assertEqual(factorial(0), 1)

    def test_1_digit(self):
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(9), 362880)

    def test_negative(self):
        self.assertEqual(factorial(-1), -1)
        self.assertEqual(factorial(-3), -6)
        self.assertEqual(factorial(-9), -362880)


if __name__ == "__main__":
    unittest.main()

```

# Find all factorial numbers less than or equal to n

## Problem

A number n is called a factorial number if it is the factorial of a positive integer. For example, the first few factorial numbers are 1, 2, 6, 24, 120. Given a number n, the task is to return the list/vector of the factorial numbers smaller than or equal to n.

```
1! = 1
2! = 2
3! = 6
4! = 24
5! = 120
```

## Example 1

- Input: n = 3
- Output: 1 2
- Explanation: The first factorial number is 1 which is less than equal to n. The second number is 2 which is less than equal to n, but the third factorial number is 6 which is greater than n. So we print only 1 and 2.

## Example 2

- Input: n = 6
- Output: 1 2 6
- Explanation: The first three factorial numbers are less than equal to n but the fourth factorial number 24 is greater than n. So we print only first three factorial numbers.

## Plan

### pseudocode

- start with n. output factorials < n
- return array

1. return an array of factorials of n
2. return factorials < n

### domain

- domain: $1 <= n <= 10^{18}$
- error case:
  - n < 0: input constrained to domain by calling function
- edge case:
  - $10^{18}$: Fits in computer memory when iterative approach is used

## Code

### brute force

Time complexity: $O(n^3)$

```python
from functools import reduce


def factorialList(n: int) -> list[int]:
    if n > 1:
        return factorialList(n - 1) + [factorial(n)]
    else:
        return [1]


def factorialNumbers(n: int) -> list[int]:
    return reduce(
        lambda factorial_list, element: (
            factorial_list + [element] if element <= n else factorial_list
        ),
        factorialList(n),
        [],
    )


import unittest


class TestFactorialList(unittest.TestCase):

    def test_1_digit(self):
        self.assertEqual(factorialList(1), [1])
        self.assertEqual(factorialList(3), [1, 2, 6])


class TestFactorialNumbers(unittest.TestCase):

    def test_1_digit(self):
        self.assertEqual(factorialNumbers(1), [1])
        self.assertEqual(factorialNumbers(3), [1, 2])
        self.assertEqual(factorialNumbers(5), [1, 2])
        self.assertEqual(factorialNumbers(6), [1, 2, 6])


if __name__ == "__main__":
    unittest.main()
```

### optimal

Time complexity: $O(n)$

```python
def factorialNumbers(n: int) -> list[int]:
    result = []
    factorial = 1
    index = 1

    while factorial <= n:
        result.append(factorial)
        index += 1
        factorial *= index

    return result


import unittest


class TestFactorialNumbers(unittest.TestCase):

    def test_1_digit(self):
        self.assertEqual(factorialNumbers(1), [1])
        self.assertEqual(factorialNumbers(3), [1, 2])
        self.assertEqual(factorialNumbers(5), [1, 2])
        self.assertEqual(factorialNumbers(6), [1, 2, 6])

    def test_large_number(self):
        self.assertEqual(
            factorialNumbers(10**18),
            [
                1,
                2,
                6,
                24,
                120,
                720,
                5040,
                40320,
                362880,
                3628800,
                39916800,
                479001600,
                6227020800,
                87178291200,
                1307674368000,
                20922789888000,
                355687428096000,
                6402373705728000,
                121645100408832000,
            ],
        )


if __name__ == "__main__":
    unittest.main()
```
