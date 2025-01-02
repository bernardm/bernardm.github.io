## problem analysis

### Example 1

- Input: N = 12345
- Output: 5
- Explanation: The number 12345 has 5 digits.

### Example 2

- Input: N = 7789
- Output: 4
- Explanation: The number 7789 has 4 digits.

## domain analysis

- domain: $$ -{\infty} < n < {\infty} $$
- error case
  - NaN -- handled by complier
- edge case: none

## code

```python
import math
import unittest


def countDigits_On(n: int) -> int:
    # dividend / divisor = quotient + remainder / divisor
    dividend = abs(n)
    count = 1

    while True:
        dividend //= 10
        if dividend == 0:
            break
        count += 1

    return count


def countDigits_O1(n: int) -> int:
    return 1 if n == 0 else int(math.log10(abs(n)) + 1)


class AbstractTestCase(object):

    def test_count_number_0(self):
        self.assertEqual(self.function(0), 1)

    def test_count_positive_digits(self):
        self.assertEqual(self.function(1), 1)
        self.assertEqual(self.function(10), 2)
        self.assertEqual(self.function(100), 3)

    def test_count_negative_digits(self):
        self.assertEqual(self.function(-100), 3)


class Test_countDigits_On(AbstractTestCase, unittest.TestCase):
    def function(self, param):
        return countDigits_On(param)


class Test_countDigits_O1(AbstractTestCase, unittest.TestCase):
    def function(self, param):
        return countDigits_O1(param)


if __name__ == "__main__":
    unittest.main()
```
