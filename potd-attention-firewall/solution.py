import numpy as np
import math

def softmax(s):
    s = np.array(s)
    exp_s = np.exp(s - np.max(s))
    return exp_s / np.sum(exp_s)
    
        

def attention_firewall(
    q: np.ndarray, keys: np.ndarray, values: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    """
    q: array of shape (d,), the query for the final position.
    keys: array of shape (n, d).
    values: array of shape (n, dv).

    s_j = (q . keys[j]) / sqrt(d)
    p = softmax(s) (numerically stable, max-subtracted)
    o = sum_j p_j * values[j]

    Returns (p, o): the attention probabilities (shape (n,)) and the
    output vector (shape (dv,)).
    """
    # TODO: scale the dot products by 1/sqrt(d), softmax them stably,
    # then take the weighted sum over values.
    d = len(q)
    s = []
    for k in keys:
        s.append((np.dot(q, k))/math.sqrt(d))
    p = softmax(s)
    o = []
    for i in range(len(p)):
        o.append(p[i] * values[i])
    o = np.sum(o, axis=0)
    return (p, o)
