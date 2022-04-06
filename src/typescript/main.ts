const start = performance.now();
const rounds: number = parseInt(await Deno.readTextFile("../rounds.txt"));

let primes: number = 1, composites: number = 1;

for (let num = 0; num <= rounds; num++) {
    let ctr = 0;

    for (let i = 2; i <= num / 2; i++) {
        if (num % i === 0) {
            ctr++;
            composites++;
            break;
        }
    }

    if (ctr === 0 && num != 1) {
        primes += 1;
    }
}

const end = performance.now() - start;
console.log(Deno.version.deno, end / 1000);
