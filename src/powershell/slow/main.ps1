$start = [Diagnostics.Stopwatch]::StartNew()
$rounds = Get-Content -Path ../../rounds.txt

$primes = 0
$composites = 0


for ($num = 0; $num -le $rounds; $num++) {
    $ctr = 0
    for ($i = 2; $i -le $num / 2; $i++) {
        if ($num % $i -eq 0) {
            $ctr++
            $composites++
            break
        }
    }
    if ($ctr -eq 0 -and $num -ne 1) {
        $primes++
    }
}
$end = $start.ElapsedMilliseconds / 1000
$version = "{0}.{1}.{2}" -f $PSVersionTable.PSVersion.Major, $PSVersionTable.PSVersion.Minor, $PSVersionTable.PSVersion.Patch
Write-Host "$version $end"