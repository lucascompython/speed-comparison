import "dart:io";
void main() {
    Stopwatch sw = new Stopwatch()..start();

    String rounds_str = new File("../../rounds.txt").readAsStringSync();
    var rounds = int.parse(rounds_str);

    var composites = 0;
    var primes = 0;


    for (int i = 0; i < rounds ; i++) {
        var ctr = 0;

        for (int k = 2; k < i / 2; k++) {
            if (i % k == 0) {
                ctr++;
                composites++;
                break;
            }
        }

        if (ctr == 0 && i != 0) {
            primes++;
        } 
    }
    var time = sw.elapsedMilliseconds / 1000;
    var version = Platform.version.split(" ")[0];
    print("$version $time");
}
