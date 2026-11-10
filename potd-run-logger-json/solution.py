def build_run_record(
    run_id: str, hyperparameters: list[tuple[str, str]], metrics: list[tuple[str, str]]
) -> dict:
    """
    Build a canonical training-run record.

    run_id: the run's id.
    hyperparameters: (key, value) pairs, in input order, keys may repeat.
    metrics: (key, value) pairs, same shape.

    Return {"run_id": run_id, "hyperparameters": {...}, "metrics": {...}}.
    Within each inner dict, keys are sorted alphabetically. A repeated key
    keeps its LAST value (later pairs overwrite earlier ones). An empty
    list of pairs gives an empty {} for that field, not an omitted key.
    """
    # TODO: build each inner dict first (last-write-wins falls out of plain
    # dict assignment), then rebuild it sorted by key.
    js = {'run_id':run_id}
    temp = dict()
    for lst in hyperparameters:
        temp[lst[0]] = lst[1]
    js['hyperparameters'] = dict(sorted(temp.items()))
    temp1 = dict()
    for val in metrics:
        temp1[val[0]] = val[1]
    js['metrics'] = dict(sorted(temp1.items()))
    return js
