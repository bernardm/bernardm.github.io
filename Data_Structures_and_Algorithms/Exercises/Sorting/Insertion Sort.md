# Insertion Sort

## Problem analysis

Insertion Sort builds the sorted portion of the array one element at a time. It takes the next unsorted element and places it in its correct position relative to the already sorted portion.

### Process (Visualization)

Input: $arr = [12, 11, 13, 5, 6]$
Output: $arr = [5, 6, 11, 12, 13]$

1. **Pass 1**:
   Compare $11$ with $12$ and place $11$ before $12$.
   Result: $[11, 12, 13, 5, 6]$.

2. **Pass 2**:
   Compare $13$ with the sorted portion ($[11, 12]$). No change.
   Result: $[11, 12, 13, 5, 6]$.

3. **Pass 3**:
   Compare $5$ with the sorted portion ($[11, 12, 13]$) and insert $5$ at the beginning.
   Result: $[5, 11, 12, 13, 6]$.

4. **Pass 4**:
   Compare $6$ with the sorted portion ($[5, 11, 12, 13]$) and insert $6$ after $5$.
   Result: $[5, 6, 11, 12, 13]$.

## Data analysis -- Iterative

- domain: $0 <= array.length <= 10^3$
- error case: None

- edge case

  - []: return []
  - [1]: return [1]
  - [2,1]: return [1,2]

- variables
  - arr -- array to sort in place
  - arr_len -- length of the array
  - boundary_ix -- start index position of the sorted array

## Data analysis -- Recursive

- domain: $0 <= array.length <= 10^3$
- error case:

  - stack overflow: use trampoline

- edge case

  - []: return []
  - [1]: return [1]

- variables
  - arr -- array to sort in place
  - arr_len -- length of the array
  - boundary_ix -- start index position of the unsorted array
