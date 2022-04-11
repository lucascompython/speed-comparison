var start = System.Diagnostics.Stopwatch.StartNew();

var rounds = Int32.Parse(System.IO.File.ReadAllText("../../rounds.txt"));


bool[] total = new bool[rounds + 1];
for (int i = 0; i <= rounds; i++)
    total[i] = true;

for (int i = 2; i <= Math.Sqrt(rounds); i++) {
    if (total[i] == true) {
        for (int j = i * i; j < rounds; j += i) {
            total[j] = false;
        }
    }
}

int primes = 0;
for (int k = 2; k < rounds; k++) {
    if (total[k] == true) {
        primes++;
    }
}

int composites = rounds - primes;



start.Stop();
var end = start.ElapsedMilliseconds;
Console.Write("{0} {1}", Environment.Version, (float)end / 1000);