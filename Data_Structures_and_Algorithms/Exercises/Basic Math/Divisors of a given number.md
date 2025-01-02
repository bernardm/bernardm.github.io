# Divisors of a given number

Given an integer N, return all divisors of N.

A divisor of an integer N is a positive integer that divides N without leaving a remainder. In other words, if N is divisible by another integer without any remainder, then that integer is considered a divisor of N.

## problem analysis

### Example 1

- Input: N = 36
- Output: [1, 2, 3, 4, 6, 9, 12, 18, 36]

```
dividend / divisor = quotient
36 / 1 = 36
36 / 2 = 18

divisor * quotient = dividend
 1 * 36 = 36 : ans
 2 * 18 = 36 : ans
 3 * 12 = 36 : ans
 4 *  9 = 36 : ans
 6 *  6 = 36 : ans
 9 *  4 = 36
12 *  3 = 36
18 *  2 = 36
```

### Example 2

- Input: N = 12
- Output: [1, 2, 3, 4, 6, 12]
- Explanation: The divisors of 12 are 1, 2, 3, 4, 6, 12.

## algorithm analysis

- loop while dividend < divisor

## domain analysis

- domain: $-{\infty} < n < {\infty}$

- error case

  - NaN -- handled by complier
  - out of memory -- crash
  - 0: throw error

- edge case: none

## code

- Time complexity: $O(\sqrt{n})$

```python
def listOfDivisors(n: int) -> list[int]:
    DIVIDEND = abs(n)

    if DIVIDEND == 0:
        raise ValueError("n cannot be 0. Zero has an infinite number of divisors.")

    # dividend / divisor = quotient + remainder / divisor
    divisor, INCREMENT = 1, DIVIDEND % 2 + 1

    divisor_list = []
    while True:
        quotient = DIVIDEND // divisor
        if quotient < divisor:
            break
        if DIVIDEND % divisor == 0:
            divisor_list.append(divisor)
            if divisor != quotient:
                divisor_list.append(quotient)
        divisor += INCREMENT

    return sorted(divisor_list)


import unittest


class TestListOfDivisors(unittest.TestCase):
    def test_divisors_of_0(self):
        with self.assertRaises(ValueError):
            listOfDivisors(0)

    def test_divisors_of_1(self):
        self.assertEqual(listOfDivisors(1), [1])
        self.assertEqual(listOfDivisors(-1), [1])

    def test_divisors_of_single_digit(self):
        self.assertEqual(listOfDivisors(4), [1, 2, 4])
        self.assertEqual(listOfDivisors(9), [1, 3, 9])

    def test_divisors_of_even_number(self):
        self.assertEqual(listOfDivisors(12), [1, 2, 3, 4, 6, 12])

    def test_divisors_of_odd_number(self):
        self.assertEqual(listOfDivisors(15), [1, 3, 5, 15])

    def test_divisors_of_negative_numbers(self):
        self.assertEqual(listOfDivisors(-12), [1, 2, 3, 4, 6, 12])

    def test_divisors_of_prime(self):
        self.assertEqual(listOfDivisors(7), [1, 7])
        self.assertEqual(listOfDivisors(151), [1, 151])


unittest.main()
```
