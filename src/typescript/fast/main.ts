const start = performance.now();
const rounds: number = parseInt(await Deno.readTextFile("../../rounds.txt"));


let total: Array<Boolean> = Array.from({length: rounds + 1}, (_, i) => true);


for (let i = 2; i <= Math.sqrt(rounds); i++) {
    if (total[i]) {
        for (let j = i * i; j <= rounds; j += i) {
            total[j] = false;
        }
    }
}

let primes: number = 0;
for (let i = 2; i <= rounds; i++) {
    if (total[i]) {
        primes++;
    }
}
let composites: number = rounds - primes;

const end = performance.now() - start;
console.log(Deno.version.deno, end / 1000);