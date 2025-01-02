# Armstrong Number

Given an integer N, return true it is an Armstrong number otherwise return false. An Amrstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

## problem analysis

### Example 1

- Input: N = 153
- Output: True
- Explanation: 1<sup>3</sup> + 5<sup>3</sup> + 3<sup>3</sup> = 1 + 125 + 27 = 153

### Example 2

- Input: N = 371
- Output: True
- Explanation: 3<sup>3</sup> + 5<sup>3</sup> + 1<sup>3</sup> = 27 + 343 + 1 = 371

## domain analysis

- domain: $0 < n < {\infty}$
- error case

  - NaN -- handled by complier
  - out of memory --

- edge case: none

## algorithm analysis

- count the digits of the number
- extract each digit, power of, sum

## variable analysis

- n: positive integer
- n_len: length of the number
- n_sum: sum of the digits of n
- digit: single digit in n
- divisor: number to extract digits from

## code

```python
import math


def countDigits(n: int) -> int:
    return 1 if n == 0 else int(math.log10(n)) + 1


def isArmstrongNumber(n: int) -> bool:
    if n < 0:
        return_value = False
    else:
        n_len, n_sum = countDigits(n), 0
        divisor = n

        while divisor > 0:
            digit, divisor = divisor % 10, divisor // 10
            n_sum += math.pow(digit, n_len)
        return_value = n == n_sum
    return return_value


import unittest


class TestCountDigits(unittest.TestCase):
    def test_count_0(self):
        self.assertEqual(countDigits(0), 1)

    def test_count_1_digit(self):
        self.assertEqual(countDigits(1), 1)

    def test_count_2_digits(self):
        self.assertEqual(countDigits(12), 2)
        self.assertEqual(countDigits(60), 2)


class TestIsArmstrongNumber(unittest.TestCase):
    def test_count_0(self):
        self.assertTrue(isArmstrongNumber(0))

    def test_examples(self):
        self.assertTrue(isArmstrongNumber(153))
        self.assertTrue(isArmstrongNumber(371))

    def test_count_negative(self):
        self.assertFalse(isArmstrongNumber(-1))


if __name__ == "__main__":
    unittest.main()
```
