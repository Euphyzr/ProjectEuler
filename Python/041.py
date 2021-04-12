from itertools import permutations
from utils import is_prime

# n = 5; 1 + 2 + 3 + 4 + 5 = 15; divisble by 3
# n = 6; ... + 6 = 21; divisable by 3
# n = 7; ... + 7 = 28; NOT divisable by 3
# n = 8; ... + 8 = 36; divsisable by 3
# n = 9; ... + 9 = 45; divisable by 3
# so only pandigitals [n] = 7 isn't divisable by 3, so it may have primes 
for perm in reversed(list(permutations(range(1, 8)))):
    n = int(''.join(map(str, perm)))
    if is_prime(n):
        print(n)
        break 