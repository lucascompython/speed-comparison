start = Time.now
rounds = File.read("../../rounds.txt")
rounds = rounds.to_i

total = []
for l in 0..rounds do total[l] = true end

for i in 2..Math.sqrt(rounds) do
    if total[i] then
        for j in (i**2..rounds).step(i) do
            total[j] = false
        end
    end
end

primes = 0
for k in 2..rounds do
    if total[k] then
        primes += 1
    end
end
composites = rounds - primes

the_end = Time.now - start
print RUBY_VERSION + " ", the_end