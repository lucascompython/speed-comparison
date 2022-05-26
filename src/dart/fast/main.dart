import "dart:io";
import "dart:math";
void main() {
    Stopwatch sw = new Stopwatch()..start();

    String rounds_str = new File("../../rounds.txt").readAsStringSync();
    int rounds = int.parse(rounds_str);

    List<bool> total = List.generate(rounds, (i) => true);

    for (int i = 2; i < sqrt(rounds); i++) {
        if (total[i]) {
            for (int j = i * i; j < rounds; j += i) {
                total[j] = false;
            }
        }
    }

    int primes = 0;
    for (int k = 2; k < rounds; k++) {
        if (total[k]) {
            primes++;
        }
    }
    int composites = rounds - primes;




    double time = sw.elapsedMilliseconds / 1000;
    String version = Platform.version.split(" ")[0];
    print("$version $time");
}