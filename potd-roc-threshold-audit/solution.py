def roc_threshold_audit(
    probs: list[float], labels: list[int], tau: float
) -> tuple[int, int, int, int, float, float]:
    """
    probs: predicted probabilities.
    labels: binary true labels (0 or 1), same length as probs.
    tau: decision threshold. Predict positive iff p_i >= tau.

    Returns (TP, FP, TN, FN, precision, recall).
    precision = TP / (TP + FP), or 0 if that denominator is 0.
    recall = TP / (TP + FN), or 0 if that denominator is 0.
    """
    # TODO: tally the confusion matrix, then compute precision and recall.
    positive = [1 if x>=tau else 0 for x in probs]
    tp=fp=tn=fn = 0
    for i in range(len(positive)):
        if positive[i] == labels[i] and positive[i]:
            tp+=1
        elif positive[i] == labels[i] and not(positive[i]):
            tn+=1
        elif positive[i] != labels[i] and positive[i]:
            fp+=1
        else:
            fn+=1
    if tp+fp==0:
        precision=0
    else:
        precision = tp/(tp+fp)
    if tp+fn==0:
        recall=0
    else:
        recall = tp/(tp+fn)
    return (tp, fp, tn, fn, precision, recall)    
        
    pass
