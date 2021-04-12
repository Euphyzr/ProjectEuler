from math import sqrt, ceil

def factorize(n):
    factors = set()
    while n % 2 == 0:
        n /= 2
        factors.add(2)

    for d in range(3, ceil(sqrt(n))+1, 2):
        while n % d == 0:
            n /= d
            factors.add(d)

    return factors

print(max(factorize(600851475143)))