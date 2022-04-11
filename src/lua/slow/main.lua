start = os.clock()
file = io.open("../../rounds.txt", "r")
rounds = file:read()

primes = 0
composites = 0

for num = 0, rounds do
    ctr = 0
    for i = 2, num / 2 do
        if num % i == 0 then
            ctr = ctr + 1
            composites = composites + 1
            break
        end
    end
    if ctr == 0 and num ~= 1 then
        primes = primes + 1
    end
end

the_end = os.clock() - start
print(_VERSION, the_end / 1000)