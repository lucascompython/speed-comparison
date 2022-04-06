const start = new Date();

const fs = require('fs');

const rounds = parseInt(fs.readFileSync("../rounds.txt").toString());
let composites = 0, primes = 0;


for (let num = 0; num <= rounds; num++) {
    let ctr = 0;

    for (let i = 2; i <= num / 2; i++) {
        if (num % i == 0) {
            ctr++;
            composites++;
            break;
        }
    }


    if (ctr == 0 && num != 1) {
        primes++;
    }
}
const end = new Date() - start;
console.log(process.version, end / 1000);
