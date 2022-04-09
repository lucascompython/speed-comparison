from time import time
start = time()
from sys import version
from math import sqrt


with open("../../rounds.txt") as f:
    rounds = int(f.read())

#implement sieve of eratosthenes
total = [True for _ in range(rounds + 1)]

for i in range(2, round(sqrt(rounds)) + 1):
    if total[i]:
        for j in range(i ** 2, rounds, i):
            total[j] = False

primes = 0
for k in range(2, rounds):
    if total[k]:
        primes += 1
composites = rounds - primes 

end = time()
print(version.split()[0], end - start, end="")
