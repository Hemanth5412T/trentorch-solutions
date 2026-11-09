# Has Duplicate

Beginner | dsa-sheet | basics | make-it-fast

Given a list of integers `nums`, return `True` if some value appears at least twice, and `False` if every value is different.

The starter code is correct, but it compares every pair of values, which is too slow for long lists. Make it fast.

### Examples

**Example 1**

Input:

```python
has_duplicate([1, 2, 3, 1])
```

Output:

```text
True
```

**Example 2**

Input:

```python
has_duplicate([1, 2, 3, 4])
```

Output:

```text
False
```

### Constraints

- `1 <= len(nums) <= 2 * 10**5`
- `-10**9 <= nums[i] <= 10**9`
