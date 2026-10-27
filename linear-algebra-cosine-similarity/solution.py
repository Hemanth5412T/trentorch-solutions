import numpy as np


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    """
    a, b: 1-D vectors of equal length.

    Returns:
        the cosine of the angle between a and b, or 0.0 if either has
        zero length.
    """
    # TODO: Dot product divided by the product of the norms.
    num=np.dot(a,b)
    den=((sum(a*a))**0.5)*((sum(b*b))**0.5)
    if den==0:
        return 0.0
    return num/den
