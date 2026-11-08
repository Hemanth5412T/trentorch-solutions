def count_pairs(n: int) -> int:
    """Return how many times `count += 1` runs."""
    # TODO: write your solution here
    if n < 2:
        return 0
    else:
        return (n-1)*(n)//2
    pass
