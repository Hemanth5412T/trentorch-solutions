import math
def count_halving_steps(n: int) -> int:
    """Return how many times the loop body runs."""
    # TODO: write your solution here
    if n > 1:
        return math.floor(math.log(n, 2))
    else:
        return 0
    pass
