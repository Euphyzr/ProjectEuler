from math import ceil, sqrt

def is_prime(n):
    if n <= 3:
        return n > 1

    if n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, ceil(sqrt(n))+1, 6):
        # n % i == 6k-1; n % (i + 2) == 6k+1
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True
