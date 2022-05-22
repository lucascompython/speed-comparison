$start = [Diagnostics.Stopwatch]::StartNew()
$rounds = Get-Content -Path ../../rounds.txt

$primes = 0
$composites = 0


#$total = 1..$rounds + 1 | foreach{$true}
$total = 1..$rounds + 1 

for ($l = 0; $l -lt $total.Count; $l++) {
    $total[$l] = $true
}

for ($i = 2; $i -le [Math]::Floor([Math]::Sqrt($rounds)); $i++) {
    if ($total[$i]) {
        for ($j = $i * $i; $j -le $rounds; $j += $i) {
            $total[$j] = $false
        }
    }
}

$primes = 0
for ($k = 2; $k -le $rounds; $k++) {
    if ($total[$k]) {
        $primes++
    }
}
$composites = $rounds - $primes


$end = $start.ElapsedMilliseconds / 1000
$version = "{0}.{1}.{2}" -f $PSVersionTable.PSVersion.Major, $PSVersionTable.PSVersion.Minor, $PSVersionTable.PSVersion.Patch
Write-Host "$version $end"