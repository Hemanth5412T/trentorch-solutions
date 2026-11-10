
import numpy as np

def soft_max(s):
    s = np.array(s)
    exp_s = np.exp(s - np.max(s))
    return exp_s / np.sum(exp_s)


def attention_firewall(q, keys, values):

    # Step 1: Calculate scaled dot-product attention scores
    d = len(q)
    s = []

    for i in range(len(keys)):
        score = np.dot(q, keys[i])
        score = score / np.sqrt(d)
        s.append(score)

    # Step 2: Calculate attention probabilities
    p = soft_max(s)

    # Step 3: Calculate weighted sum of values
    o = np.sum(p[:, np.newaxis] * values, axis=0)

    return p, o
