from utils import is_prime

prime_count = 0
n = 1
while prime_count < 10001:
    n += 1
    if is_prime(n):
        prime_count += 1

print(n, prime_count)