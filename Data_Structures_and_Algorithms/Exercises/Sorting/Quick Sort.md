# Quick Sort

## Problem analysis

Quick Sort is a divide-and-conquer algorithm. The array is divided into two subarrays based on a pivot element, and the subarrays are sorted recursively.

### Process (Visualization)

Input: $arr = [1, 2, 4, 0, 5, 3]$
Output: $arr = [0, 1, 2, 3, 4, 5]$

1. Choose a Pivot:
   Select the last element of the list as the _pivot value_ $3$

2. Partition the Array:
   Rearrange elements so that all elements smaller than the pivot appear before it, and all elements larger appear after it.
   Result: $[1, 2, 0, 3, 5, 4]$
   $3$ is now in its correct position.

   1. Select the last element as the _pivot value_.
   1. Move the left bound to the right until it reaches a value greater than or equal to the pivot.
      - Using `left_ix`, sweep the array from left to right while it is < _pivot value_
   1. Move the right bound to the left until it crosses the left bound or finds a value less than the pivot.
      - Using `right_ix`, sweep the array from the right to the left while it is >= _pivot value_
   1. Check if partitioning is complete
      ```python
      if left_ix >= right_ix:
         # swap values referenced by `left_ix` and `pivot_ix`
         # partitioning complete
      else:
         # swap values referenced by `left_ix` and `right_ix`
      ```

3. Recursive Sort:
   Recursively apply the same process to the subarrays:
   $[1, 2, 0]$ and $[5, 4]$.

4. Repeat Until Sorted:
   Continue recursively partitioning until each subarray contains a single element or is empty.

## Data analysis

- domain: $0 <= array.length <= 10^3$
- error case: None
- edge case

  - []: return []
  - [1]: return [1]

- variables
  - arr -- array to be sorted
  - left_ix -- left index of the array
  - right_ix -- right index of the array
  - pivot_ix -- last position in the array
  - pivot_value -- element value
