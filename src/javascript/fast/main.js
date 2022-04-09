const start = new Date();

const fs = require('fs');

const rounds = parseInt(fs.readFileSync("../../rounds.txt").toString());


let total = Array.from({length: rounds + 1}, (_, i) => true);

for (let i = 2; i <= Math.sqrt(rounds); i++) {
    if (total[i]) {
        for (let j = i * i; j <= rounds; j += i) {
            total[j] = false;
        }
    }
}

let primes = 0;
for (let i = 2; i <= rounds; i++) {
    if (total[i]) {
        primes++;
    }
}
let composites = rounds - primes;

const end = new Date() - start;
console.log(process.version.substring(1), end / 1000);
