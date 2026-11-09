# How Big Can n Be?

Intermediate | dsa-sheet | basics | counting-steps

You have a budget of basic operations. An algorithm's cost on an input of size `n` is given by its growth class. Find the largest `n` you can afford.

The cost of size `n` is:

| `growth`    | cost                                                     |
| ----------- | -------------------------------------------------------- |
| `"n"`       | `n`                                                      |
| `"n log n"` | `n * floor(log2(n))`, written `n * (n.bit_length() - 1)` |
| `"n^2"`     | `n * n`                                                  |
| `"n^3"`     | `n * n * n`                                              |
| `"2^n"`     | `2 ** n`                                                 |

Implement `largest_n(growth, budget)`. Return the largest `n >= 1` whose cost is at most `budget`, or `0` if even `n = 1` costs more than `budget`.

### Examples

**Example 1**

Input:

```python
largest_n('n^2', 100)
```

Output:

```text
10
```

`10 * 10 = 100` fits, `11 * 11 = 121` does not.

**Example 2**

Input:

```python
largest_n('n log n', 100)
```

Output:

```text
25
```

Costs: n=1 is 0, n=2 is 2, n=3 is 3, n=4 is 8, n=8 is 24 ... n=25 is 100.

### Constraints

- `0 <= budget <= 10**18`
- `growth` is one of the five strings above.
- Trying every `n` one by one is too slow for the large budgets.
