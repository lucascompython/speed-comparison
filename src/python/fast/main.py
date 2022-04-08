from time import time
start = time()
from sys import version
from math import sqrt


with open("../../rounds.txt") as f:
    rounds = int(f.read())

#implement sieve of eratosthenes
primes = [True for _ in range(rounds + 1)]

for i in range(2, round(sqrt(rounds)) + 1):
    if primes[i]:
        for j in range(i ** 2, rounds, i):
            primes[j] = False

total = 0
for k in range(2, rounds):
    if primes[k]:
        total += 1
composites = rounds - total

end = time()
print(version.split()[0], end - start, end="")
