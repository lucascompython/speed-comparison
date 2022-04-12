start = Time.now
rounds = File.read("../../rounds.txt")


primes = 0
composites = 0 
for num in 0..rounds.to_i do
    ctr = 0

    for i in 2..num / 2 do
        if num % i == 0 then
            ctr += 1
            composites += 1
            break
        end
        
    end
    if ctr == 0 and num != 1 then
        primes += 1
    end
end

the_end = Time.now - start
print RUBY_VERSION + " ", the_end