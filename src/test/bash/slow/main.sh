START=$(date +%s.%N)
rounds=$(<../../rounds.txt)



primes=0
composites=0

#for num in {0..2500}
#do
    #ctr=0
    #for i in $(seq 2 $(($num / 2))); do
        #((ctr++))
        #((composites++))
        #break
    #done

    #if [[ $ctr = 0 ]] && [[ $num != 1 ]]
    #then
        #((primes++))
    #fi
#done

#echo $primes0



for ((num = 1; num <= $rounds; num++)); do
    ctr=0

    for ((i = 2; i <= (num / 2); i++)); do
        if ((num % i == 0)); then
            ((ctr++))
            ((composites++))
            break
        fi
    done

    if ((ctr == 0)); then
        if ((num != 1)); then
            ((primes++))
        fi
    fi
done
END=$(date +%s.%N)
DIFF=$(echo "$END - $START" | bc)
echo "$BASH_VERSION $DIFF"