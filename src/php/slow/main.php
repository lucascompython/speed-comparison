<?php
$start = microtime(true);
$file = fopen("../../rounds.txt", "r");
$rounds = fread($file, filesize("../../rounds.txt"));
fclose($file);


$primes = 0;
$composites = 0;

for ($num = 0; $num <= $rounds; $num++) {
    $ctr = 0;

    for ($i = 2; $i <= $num / 2; $i++) {
        if ($num % $i == 0) {
            $ctr++;
            $composites++;
            break;
        }
    }

    if ($ctr == 0 && $num != 1) {
        $primes++;
    }
}

$end = microtime(true) - $start;
echo phpversion() . " " . $end;
?>