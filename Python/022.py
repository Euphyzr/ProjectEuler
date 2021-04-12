from names import names  # save names.txt as names.py with the names wrapped with []s as variable names
names = sorted(names)    # names.txt can be found at https://projecteuler.net/project/resources/p022_names.txt

alpha_scores = {a:n+1 for n, a in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
def get_score(name):
    return sum(alpha_scores[ch] for ch in name)

print(sum(get_score(name) * (index+1) for index, name in enumerate(names)))