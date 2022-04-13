use std::fs;
use std::process::Command;
use std::time::Instant;

fn main() {
    let start = Instant::now();
    let contents = fs::read_to_string("../../rounds.txt").expect("Something went wrong reading the file");
    let rounds = contents.trim().parse::<u32>().unwrap();
    let mut _primes = 0; let mut _composites = 0;
    for num in 0..rounds + 1 {
        let mut ctr = 0;

        for i in 2..(num + 1) / 2 {
            if num % i == 0 {
                ctr += 1;
                _composites += 1;
                break;
            }
        }

        if ctr == 0 && num != 1 {
            _primes += 1;
        }

    }
    let version = Command::new("cargo").arg("--version").output().expect("rustc not found");
    let end = start.elapsed();
    println!("{} {}", String::from_utf8_lossy(&version.stdout).replace("cargo", "").trim(), end.as_millis() as f64 / 1000.0);

}