import Foundation
let start = DispatchTime.now();


let rounds_str = try! String(contentsOfFile: "../../rounds.txt", encoding: .utf8);
let rounds = Int(rounds_str) ?? 0;

var primes: Double = 0;
var composites: Double = 0;


for num in stride(from: 0, through: rounds, by: 1){
    var ctr = 0;

    for i in stride(from: 2, through: num / 2, by: 1){
        if (num % i == 0){
            ctr += 1;
            composites += 1;
            break;
        }
    }

    if (ctr == 0 && num != 1) {
        primes += 1;
    }
}
let stop = DispatchTime.now();
let nanoTime = stop.uptimeNanoseconds - start.uptimeNanoseconds;
let timeInterval = Double(nanoTime) / 1_000_000_000;

//TODO make swift print version

print(timeInterval);