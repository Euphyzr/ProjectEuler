from utils import is_prime

_sum = 0
for n in range((2 * (10 ** 6))+1):
    if is_prime(n):
        _sum += n

print(_sum)