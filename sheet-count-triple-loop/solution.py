def count_triple_loop(n: int) -> int:
    """Return how many times `count += 1` runs."""
    # TODO: write your solution here
    ans = 0
    if n == 0:
        return 0
    while n > 0:
        ans+= (n*(n+1))//2
        n-=1
    return ans
