local start = os.clock()
local file = io.open("../../rounds.txt", "r")
local rounds = file:read()

local total = {}

for prime = 2, rounds do total[prime] = true end


for i = 2, math.sqrt(rounds) do
    if total[i] then
        for j = i * i, rounds, i do
            total[j] = false
        end
    end
end

local primes = 0
for k = 2, rounds do
    if total[k] then
        primes = primes + 1
    end
end
local composites = rounds - primes

the_end = os.clock() - start
print(_VERSION, the_end / 1000)