<?php
$start = microtime(true);
$file = fopen("../../rounds.txt", "r");
$rounds = fread($file, filesize("../../rounds.txt"));
fclose($file);


$total = array_fill(0, $rounds + 1, true);

for ($i = 2; $i <= sqrt($rounds); $i++) {
    if ($total[$i]) {
        for ($j = $i * $i; $j <= $rounds; $j += $i) {
            $total[$j] = false;
        }
    }
}


$primes = 0;
for ($i = 2; $i <= $rounds; $i++) {
    if ($total[$i]) {
        $primes++;
    }
}
$composites = $rounds - $primes;



$end = microtime(true) - $start;
echo phpversion() . " " . $end;
?>