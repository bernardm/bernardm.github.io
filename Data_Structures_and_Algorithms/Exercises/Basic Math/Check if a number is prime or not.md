# Check if a number is prime or not

Given an integer N, check whether it is prime or not. A prime number is a number that is only divisible by 1 and itself and the total number of divisors is 2.

## Problem analysis

### Example 1

- Input: N = 2
- Output: true
- Explanation: 2 is a prime number because it has two divisors: 1 and 2 (the number itself).

### Example 2

- Input: N =10
- Output: false
- Explanation: 10 is not prime, it is a composite number because it has 4 divisors: 1, 2, 5 and 10.

## Data analysis

- domain: $-{\infty} < n < {\infty}$
- error case:

  - float: compiler
  - NaN: compiler

- edge case:
  - n < 0: abs(n)
  - n == 0: false
  - n == 1: false

## Algorithm analysis

- given:
  - even numbers are not prime
  - only need to test numbers from 3 to sqrt(n)

```
n = 16

1, 16
2, 8
4, 4 <- sqrt(n)

```

## Code

```python
import math


def isPrime(n: int) -> bool:
    """
    Check if a number is prime.
    Time complexity: O(sqrt(n))

    :param n: The number to check.
    :return: True if the number is prime, False otherwise.
    """

    n = abs(n)

    if n <= 1:
        return False
    if n % 2 == 0:
        return False

    for divisor in range(3, int(math.sqrt(n)) + 1):
        if n % divisor == 0:
            return False

    return True


import unittest


class TestIsPrime(unittest.TestCase):
    def test_prime_of_0(self):
        self.assertFalse(isPrime(0))

    def test_prime_of_1(self):
        self.assertFalse(isPrime(1))

    def test_prime_of_single_digit(self):
        self.assertFalse(isPrime(4))
        self.assertFalse(isPrime(9))

    def test_prime_of_even_number(self):
        self.assertFalse(isPrime(12))

    def test_prime_of_odd_number(self):
        self.assertFalse(isPrime(15))

    def test_prime_of_negative_numbers(self):
        self.assertFalse(isPrime(-12))

    def test_prime_of_prime(self):
        self.assertTrue(isPrime(7))
        self.assertTrue(isPrime(151))


unittest.main()
```
