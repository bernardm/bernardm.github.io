# Greatest Common Divisor

## problem analysis

### Example 1

Input: N1 = 9, N2 = 12

Output: 3

Explanation:

- Factors of 9: 1, 3, 9
- Factors of 12: 1, 2, 3, 4, 6, 12
- Common Factors: 1, 3
- Greatest Common Factor: 3

### Example 2

Input: N1 = 20, N2 = 15

Output: 5

Explanation:

- Factors of 20: 1, 2, 4, 5
- Factors of 15: 1, 3, 5
- Common Factors: 1, 5
- Greatest Common Factor: 5

## domain analysis

- domain:

  - 0 < n < infinity

- error:

  - NaN -- compiler will handle that
  - n <= 0:
    - 0 -- throw error
    - n < 0 -- abs(n)

- edge:
  - outside domain:
    - 0:
      - gcd(100,0) = 100
      - gcd(0,0) = infinity
  - 1: return [1]
  - 2: return [1,2]

## code - O(n $^2$)

```python
def integerDivisorsOf(n: int) -> list[int]:
    dividend = abs(n)
    lower_bound = 2
    upper_bound = n // 2 + 1

    # dividend / divisor = quotient + remainder / divisor
    divisorList = set([1, dividend])
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 2]
    elif n == 3:
        return [1, 3]
    else:
        for divisor in range(lower_bound, upper_bound):
            if dividend % divisor == 0:
                divisorList.add(divisor)
                divisorList.add(dividend)

    return divisorList


def gcd(n1: int, n2: int) -> int:
    d1 = integerDivisorsOf(n1)
    d2 = integerDivisorsOf(n2)

    return max(d1.intersection(d2))
```

## code - O(min(n1, n2))

```python
def gcd(a: int, b: int) -> int:
    """
    Find the GCD of the given integers.

    The Greatest Common Divisor is the largest number that divides the given integers. This function uses the Euclidean Algorithm. It operates on the principle that the GCD of two numbers remains the same even if the smaller number is subtracted from the larger number.
    """
    # Dividend / Divisor = Quotient + Remainder / Divisor
    dividend, divisor = abs(a), abs(b)

    if dividend < divisor:
        dividend, divisor = divisor, dividend

    while divisor != 0:
        dividend, divisor = divisor, dividend % divisor
    return dividend
```
