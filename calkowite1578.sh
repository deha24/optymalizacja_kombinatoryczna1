#!/bin/bash
# KTZ 2025
# plik: calkowite15.sh
#./calkowite15.sh 15 21 $((2**31)) 0

n=$1
e=$2
mod=$3
pierwszy=$4

echo czas: $(date)

for (( res=$pierwszy; res < $mod ; res+=1 ))
do
 echo "time ./geng -c $n $e:$e $res/$mod 2>/dev/null | ./sito5 640000 | tee -a wynik15_78.txt"
 echo "./calkowite1578.sh $n $e $mod $res" > ktz2025_todo15.sh
 time ./geng -c $n $e:$e $res/$mod 2>/dev/null | ./sito5 640000 | tee -a wynik15_78.txt
done

echo czas: $(date)
echo "# wszystko zrobione " > ktz2025_todo15.sh
