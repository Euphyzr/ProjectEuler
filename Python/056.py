_max = 0
a, b = 1, 101

for base in range(a, b):
    for exp in range(a, b):
        result = base ** exp
        _sum = sum(map(int, str(result)))
        if _sum > _max:
            _max = _sum

print(_max)