def cal_cost(n, growth, budget):
    if growth == 'n':
        return n
    elif growth == 'n log n':
        return n * (n.bit_length() - 1)
    elif growth == 'n^2':
        return n * n
    elif growth == 'n^3':
        return n * n * n
    else:
        if n >= budget.bit_length():
            return budget + 1
        return 2**n


def largest_n(growth: str, budget: int) -> int:
    lo, hi = 1, budget + 1
    ans = 0

    while lo <= hi:
        mid = (lo + hi) // 2

        if cal_cost(mid, growth, budget) <= budget:
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1

    return ans
