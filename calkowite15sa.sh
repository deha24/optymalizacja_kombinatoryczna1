#!/bin/bash
# KTZ 2025 
# plik: calkowite15sa.sh
#./calkowite15sa.sh 15 27 20 0.99998 500000 100
 
n=$1
k=$2
temp=$3
cooling=$4
max_rep=$5
rep=$6

echo czas: $(date)  
 
for (( res=0; res < $rep ; res+=1 ))
do 
 echo "time python3 simulatedAnnealing.py $n $k $temp $cooling $max_rep 1 2>/dev/null | ./sito5 | tee -a wynik15.txt"
 echo "./calkowite15sa.sh $n $k $temp $cooling $max_rep" > ktz2025_todo15.sh
 time  python3 simulatedAnnealing.py $n $k $temp $cooling $max_rep 1 2>/dev/null | ./sito5 | tee -a wynik15.txt
done 
 
echo czas: $(date) 
echo "# wszystko zrobione " > ktz2025_todo15.sh
