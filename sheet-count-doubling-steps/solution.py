import math
def count_doubling_steps(n: int) -> int:
    """Return how many times the loop body runs."""
    # TODO: write your solution here
    count = 0
    i = 1
    while i < n:
        i *= 2
        count += 1
    return count
