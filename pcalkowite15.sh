#!/bin/bash
# KTZ 2025 
# plik: pcalkowite15.sh
#./pcalkowite15.sh 15 21 $((2**31)) 0 
 
n=$1
e=$2
mod=$3
pierwszy=$4
 
echo czas: $(date)  
 
for (( res=$pierwszy; res < $mod ; res+=1 ))
do 
 echo "time ./geng -c $n $e:$e $res/$mod 2>/dev/null | ./sito2 | tee -a wynikp15.txt"
 echo "./calkowite15.sh $n $e $mod $res" > ktz2025_todo15.sh
 time ./geng -c $n $e:$e $res/$mod 2>/dev/null | ./sito2 | tee -a wynikp15.txt
done 
 
echo czas: $(date) 
echo "# wszystko zrobione " > ktz2025_todo15.sh
