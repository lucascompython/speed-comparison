import Foundation
let start = DispatchTime.now();


let rounds_str = try! String(contentsOfFile: "../../rounds.txt", encoding: .utf8);
let rounds = Int(rounds_str) ?? 0;
let rounds_sqrt = Int(round(Double(rounds).squareRoot()));

//populate the array
var total = [Bool] (repeating: true, count: rounds + 1);

for i in stride(from: 2, through: rounds_sqrt, by: 1) {
    if (total[i]) {
        for j in stride(from: i * i, through: rounds, by: i) {
            total[j] = false;
        }
    }
}

var primes = 0;
for k in stride(from: 2, through: rounds, by: 1) {
    if (total[k]) {
        primes += 1;
    }
}



let stop = DispatchTime.now();
let nanoTime = stop.uptimeNanoseconds - start.uptimeNanoseconds;
let timeInterval = Double(nanoTime) / 1_000_000_000;

//TODO make swift print version
print(timeInterval);


