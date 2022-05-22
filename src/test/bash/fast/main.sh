START=$(date +%s.%N)
rounds=$(<../../rounds.txt)

square="$(echo "sqrt($rounds)" | bc)"
rounded=$(echo $square | awk '{printf int($1+0.5)}')


#declare -a total=()
for ((i = 0; i < rounds; i++)); do
    #((total[i] = true))
    #total+=(1)
    total[$i]=1
done

#for ((i = 2; i <= rounded; i++)); do
    #if [[ total[i] ]]; then
        #for ((j = i * i; j <= rounds; j += i)); do
            #total[j]=false
        #done
    #fi
#done


#primes=0
#for k in 2..$rounds; do
    #if [[ $total[$k] ]]; then
        #((primes++))
    #fi
#done
#composites=$((rounds - primes))

for i in $(seq 2 $rounded)
do
    if  [[ total[i] -eq 1 ]] 
    then
        #for j in $(seq $(($i**2)) $rounds $i)
        #do
            #echo "ola"
            #total[j]=false
        #done
        for ((j = i*i; j <= rounds; j += i)); do
            echo "ola"
            total[$j]=0
        done
    fi
done

primes=0
for k in $(seq 2 $rounds)
do
    if [ total[$k] -eq 1 ]
    then
        primes=$((primes+1))
    fi
done



echo $primes ${#primes[@]}






END=$(date +%s.%N)
DIFF=$(echo "$END - $START" | bc)
echo "$BASH_VERSION $DIFF"
#i hate bash so fucking much