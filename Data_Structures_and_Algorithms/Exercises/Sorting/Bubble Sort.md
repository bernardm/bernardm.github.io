# Bubble Sort

Implement the Bubble sorting algorithm.

# Problem analysis

Bubble Sort works by repeatedly swapping adjacent elements that are in the wrong order. This process is repeated until no swaps are needed.

### Process (Visualization)

Input: $arr = [64, 34, 25, 12, 22, 11, 90]$
Output: $arr = [11, 12, 22, 25, 34, 64, 90]$

1. Pass 1:
   Compare adjacent elements and swap if needed:
   $[64, 34, 25, 12, 22, 11, 90]$ → $[34, 25, 12, 22, 11, 64, 90]$
   Largest element $90$ is moved to the correct position.

2. Pass 2:
   Repeat for the remaining unsorted portion:
   $[34, 25, 12, 22, 11, 64, 90]$ → $[25, 12, 22, 11, 34, 64, 90]$

3. Pass 3:
   Continue:
   $[25, 12, 22, 11, 34, 64, 90]$ → $[12, 22, 11, 25, 34, 64, 90]$

4. Pass 4:
   $[12, 22, 11, 25, 34, 64, 90]$ → $[12, 11, 22, 25, 34, 64, 90]$

5. Pass 5:
   $[12, 11, 22, 25, 34, 64, 90]$ → $[11, 12, 22, 25, 34, 64, 90]$

6. Pass 6:
   Array is sorted.

# Data analysis -- Iterative

- domain: $0 <= array.length <= 10^3$
- error case:

  - elements have different data types, therefore they cannot be compared:

- edge case

  - []: return []
  - [1]: return [1]

- variables
  - arr -- array to be sorted
  - arr_len -- length of the entire array
  - boundary_len -- length of the unsorted half of the array

# Data analysis -- Recursive

- domain: $0 <= array.length <= 10^3$
- error case: None
- edge case

  - []: return []
  - [1]: return [1]

- variables
  - arr -- array to be sorted
  - partition_len -- length of the unsorted part of the array
