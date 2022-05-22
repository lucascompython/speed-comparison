#!/bin/bash
limit=$1
sieve="$(seq 2 $limit|sort)"

for n in 2 $(seq 3 2 $limit)
do
  sieve="$(comm -23 <(echo "$sieve") <(seq $(($n * $n)) $n $limit|sort))"
done

sorted="$(echo "$sieve"|sort -n)"
#echo $sorted
#$(python -c "print('ola from python')")
python3 <<< 'print(len("$sorted".split()))'