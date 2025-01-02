# Reverse Digits of A Number

## problem analysis

Given an integer N return the reverse of the given number. If a number has trailing zeros, then its reverse will not include them. For e.g., reverse of 10400 will be 401 instead of 00401.

### Example 1

- Input: N = 12345
- Output: 54321
- Explanation: The reverse of 12345 is 54321.

### Example 2

- Input: N = 7789
- Output: 9877
- Explanation: The reverse of number 7789 is 9877.

## algorithm analysis

- remove the lowest digit of a number
- add to to the reversed number

## domain analysis

- domain: $-{\infty} < n < {\infty}$
- error case:
  - NaN -- handled by complier
- edge case: none

## code

```python
def reverseNumber(n: int) -> int:
    # dividend / divisor = quotient + remainder / divisor
    dividend = abs(n)
    reverse_number = 0

    while dividend > 0:
        digit = dividend % 10
        dividend //= 10
        reverse_number = reverse_number * 10 + digit
    return reverse_number if n >= 0 else -reverse_number


import unittest


class TestReverseNumber(unittest.TestCase):
    def test_reverse_0(self):
        self.assertEqual(reverseNumber(0), 0)

    def test_reverse_has_1_digit(self):
        self.assertEqual(reverseNumber(1), 1)
        self.assertEqual(reverseNumber(10), 1)
        self.assertEqual(reverseNumber(100), 1)

    def test_reverse_negative(self):
        self.assertEqual(reverseNumber(-121), -121)

    def test_reverse_positive(self):
        self.assertEqual(reverseNumber(12345), 54321)


if __name__ == "__main__":
    unittest.main()
```

## problem analysis

There is a song concert going to happen in the city. The price of each ticket is equal to the number obtained after reversing the bits of a given 32 bits unsigned integer ‘n’.

### Example 1:

- Input: N = 12
- Output: 805306368
- Explanation: Since the given number N = 12 is represented as 00000000000000000000000000001100 in its binary representation. So after reversing the bits, it will become 0110000000000000000000000000000, which is equal to 805306368

### Example 1:

- Input: N = 6
- Output: 1610612736
- Explanation: Since the given number N = 6 is represented as 00000000000000000000000000000110 in its binary representation. So after reversing the bits, it will become 01100000000000000000000000000000, which is equal to 1610612736

## algorithm analysis

- pop off the lest significant (right hand) binary digit
- add it to the reverse_number
- do this 32 times

## domain analysis

- domain: $-{\infty} < n < {\infty}$
- error case:
  - NaN -- handled by complier
- edge case: none

## variable analysis

## code

```python
def reverseBits(n: int) -> int:
    # dividend / divisor = quotient + remainder / divisor
    dividend = abs(n)
    reverse_number = 0

    for _ in range(32):
        digit = dividend % 2
        dividend //= 2
        reverse_number = reverse_number * 2 + digit
    return reverse_number if n >= 0 else -reverse_number


import unittest


class TestReverseBits(unittest.TestCase):
    def test_reverse_0(self):
        self.assertEqual(reverseBits(0), 0)

    def test_reverse_1_digit(self):
        self.assertEqual(reverseBits(1), 2147483648)  # 2^31

    def test_reverse_examples(self):
        self.assertEqual(reverseBits(12), 805306368)
        self.assertEqual(reverseBits(6), 1610612736)

    def test_reverse_negative(self):
        self.assertEqual(reverseBits(-1), -2147483648)  # -@^31


if __name__ == "__main__":
    unittest.main()
```
