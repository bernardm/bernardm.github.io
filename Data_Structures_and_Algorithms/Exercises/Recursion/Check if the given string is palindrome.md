# Check if the given string is palindrome

Given a string, check if the string is palindrome or not. A string is said to be palindrome if the reverse of the string is the same as the string.

## Problem analysis

### Example 1

- Input: s = "A man, a plan, a canal: Panama"
- Output: true
- Explanation: "amanaplanacanalpanama" is a palindrome.

### Example 2

- Input: s = "race a car"
- Output: false
- Explanation: "raceacar" is not a palindrome.

### Example 3

- Input: s = ""
- Output: true
- Explanation: An empty string reads the same forward and backward, it is a palindrome.

### Example 4

- Input: s = “ABCDCBA”
- Output: true
- Explanation: String when reversed is the same as string.

## Data analysis

- domain: "" <= string.length < 1000
- error case: none
- edge case:
  - "": true
  - "a": true

## Algorithm analysis

```
 012
"aba"
" b "

 0123
"abba"
" bb "
```

## Code

```python
import string


def isPalindrome(input_string):
    input_string = filterLettersAndNumbers(input_string).lower()
    return _isPalindromeRecursive(input_string, 0, len(input_string) - 1)


def _isPalindromeRecursive(s, start, end):
    """
    Helper function to check if a string is a palindrome.

    Time complexity: O(n)
    Space complexity: O(n)

    :param s: input string
    :param start: start index
    :param end: end index
    :return: True if s is a palindrome, False otherwise
    """
    if start >= end:
        return True
    if s[start] != s[end]:
        return False
    return _isPalindromeRecursive(s, start + 1, end - 1)


def filterLettersAndNumbers(input_string):
    return "".join(filter(lambda char: char.isalnum(), input_string))


import unittest


class Test_isPalindrome(unittest.TestCase):
    def test_empty_string(self):
        self.assertTrue(isPalindrome(""))

    def test_single_letter(self):
        self.assertTrue(isPalindrome("a"))

    def test_single_number(self):
        self.assertTrue(isPalindrome("1"))

    def test_palindrome_odd(self):
        self.assertTrue(isPalindrome("aba"))

    def test_palindrome_even(self):
        self.assertTrue(isPalindrome("abba"))

    def test_not_palindrome(self):
        self.assertFalse(isPalindrome("abca"))


class Test_filterLettersAndNumbers(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(filterLettersAndNumbers(""), "")

    def test_no_letters_or_numbers(self):
        self.assertEqual(filterLettersAndNumbers(".,!"), "")

    def test_all_letters_and_numbers(self):
        self.assertEqual(filterLettersAndNumbers("abc123"), "abc123")

    def test_mixed_input(self):
        self.assertEqual(filterLettersAndNumbers("abc!123!"), "abc123")


unittest.main()
```
