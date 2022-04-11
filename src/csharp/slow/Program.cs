var start = System.Diagnostics.Stopwatch.StartNew();

var rounds = Int32.Parse(System.IO.File.ReadAllText("../../rounds.txt"));



int primes = 0, composites = 0;

for(int num = 0; num <= rounds; num++){
    int ctr = 0;

    for(int i = 2; i <= num / 2; i++){
        if(num % i == 0){
            ctr++;
            composites++;
            break;
        }
    }

    if(ctr == 0 && num != 1){
        primes++;
    }
}
start.Stop();
var end = start.ElapsedMilliseconds;
Console.Write("{0} {1}", Environment.Version, (float)end / 1000);