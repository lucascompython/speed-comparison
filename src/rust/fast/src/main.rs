use std::fs::File;
use std::io::Read;
use std::process::Command;
use std::time::Instant;

fn main() {
    let start = Instant::now();
    let mut f = File::open("../../rounds.txt").unwrap();
    let mut rounds = String::new();
    f.read_to_string(&mut rounds).unwrap();
    let rounds: i32 = rounds.trim().parse().unwrap();

    let mut total = vec![true; rounds as usize + 1];

    for i in 2..rounds as usize {
        if total[i] {
            for j in (i * i..rounds as usize).step_by(i) {
                total[j] = false;
            }
        }
    }

    let mut primes = 0;
    for k in 2..rounds as usize {
        if total[k] {
            primes += 1;
        }
    }
    let _composites = rounds - primes;
    
    let version = Command::new("cargo").arg("--version").output().expect("rustc not found");
    let end = start.elapsed();
    println!("{} {}", String::from_utf8_lossy(&version.stdout).replace("cargo", "").trim(), end.as_millis() as f64 / 1000.0);

}