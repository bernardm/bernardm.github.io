# Selection Sort

Implement the Selection sorting algorithm.

## Problem analysis

Selection Sort is a simple sorting algorithm that repeatedly selects the smallest element from the unsorted portion of the array and swaps it with the first element of the unsorted portion.

### Process (Visualization)

Input: $arr = [64, 25, 12, 22, 11]$
Output: $arr = [11, 12, 22, 25, 64]$

1. Pass 1:

- Find the smallest element in the entire array ($11$).
- Swap it with the first element.
- Result: $[11, 25, 12, 22, 64]$.

2. Pass 2:

- Find the smallest element in the remaining array ($[25, 12, 22, 64]$: $12$).
- Swap it with the second element.
- Result: $[11, 12, 25, 22, 64]$.

3. Pass 3:

- Find the smallest element in the remaining array ($[25, 22, 64]$: $22$).
- Swap it with the third element.
- Result: $[11, 12, 22, 25, 64]$.

4. Pass 4:

- Find the smallest element in the remaining array ($[25, 64]$: $25$).
- Swap it with itself.
- Result: $[11, 12, 22, 25, 64]$.

5. Pass 5:

- The array is already sorted.

## Data analysis

- domain: $0 <= array.length <= 10^3$
- error case: None

- edge case

  - []: return []
  - [1]: return [1]

- variables
  - arr -- array to sort in place
  - arr_len -- length of the array
  - boundary_ix -- start index position of the unsorted array
