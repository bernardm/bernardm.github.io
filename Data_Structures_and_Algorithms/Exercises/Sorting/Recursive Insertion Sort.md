# Recursive Insertion Sort

## Problem analysis

## Data analysis

- domain: $0 <= array.length <= 1000$
- error case: None

- edge case
  - []: return []
  - [1]: return [1]

## Algorithm analysis

```
arr = [4, 3, 2, 1]

unsorted | sorted
 0  1  2  3
[4, 3, 2, 1] | []
  - begin_ix: 4
  - end_ix: 4
  - boundary_ix: 2

unsorted  | sorted
 0  1  2     3
[4, 3, 2] | [1]
  - begin_ix: 3
  - end_ix: 4
  - boundary_ix: 1

unsorted  | sorted
 0  1        2  3
[4, 3]    | [1, 2]
  - begin_ix: 2
  - end_ix: 4
  - boundary_ix: 0

unsorted | sorted
 0          1  2  3
[4]      | [1, 2, 3]

```

- variable
  - begin_ix: begin index of the sorted array
  - end_ix: end index of the sorted array
  - boundary_ix: last element of the unsorted array
