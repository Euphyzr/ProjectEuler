from itertools import permutations as pms

millionth = list(pms(range(10)))[1000000-1]

print(''.join(map(str, millionth)))