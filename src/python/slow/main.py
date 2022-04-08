import time
import sys
start = time.time()
with open("../../rounds.txt") as f:
    rounds = int(f.read())

primes = 0
composites = 0

for num in range(rounds):
    ctr = 0

    for i in range(2, num // 2):
        if num % i == 0:
            ctr += 1
            composites +=1
            break

    if ctr == 0 and num != 1:
        primes += 1
end = time.time()
print(sys.version.split()[0], end - start, end="")
