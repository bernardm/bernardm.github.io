# Recursive Bubble Sort

## Problem analysis

### Example 1

- Input: N = 6, array[] = [13,46,24,52,20,9]
- Output: 9,13,20,24,46,52
- Explanation: After sorting we get 9,13,20,24,46,52

### Example 2

- Input: N = 5, array[] = [5,4,3,2,1]
- Output: 1,2,3,4,5
- Explanation: After sorting we get 1,2,3,4,5

## Data analysis

- domain: $0 <= array.length <= 1000$
- error case: None

- edge case
  - []: return []
  - [1]: return [1]
  - [2,1]: return [1,2]

## Algorithm analysis

```
arr = [4, 3, 2, 1]

unsorted | sorted
 0  1  2  3
[4, 3, 2, 1]
begin_ix: 0
end_ix: 3
boundary_ix: 4
# sweep the 4 to the end

 0  1  2     3
[3, 2, 1] | [4]
begin_ix: 0
end_ix: 2
boundary_ix: 3
# sweep the 36 to the end

 0  1     2  3
[2, 1] | [3, 4]
begin_ix: 0
end_ix: 1
boundary_ix: 2
```

- variables
  - begin_ix -- start of the unsorted array
  - end_ix -- end of the unsorted array
  - boundary_ix -- index at which the sorted array starts. this is also the length of the unsorted array
