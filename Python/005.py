"""
Smallest multiple
~~~~~~~~~~~~~~~~~
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
from math import gcd

def lcm(numbers):
    # Smallest number that can be divided by 
    # a set of numbers is basically their LCM
    result = numbers.pop()
    for num in numbers:
        result = int((result * num) / gcd(result, num))
    
    return result

print(lcm(list(range(1, 21))))