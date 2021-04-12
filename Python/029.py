def distinct(a, b):
    results = set()
    for base in range(a, b):
        for pw in range(a, b):
            results.add(base ** pw)
    return results
print(len(distinct(2, 101)))