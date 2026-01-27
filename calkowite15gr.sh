#!/bin/bash
# KTZ 2025 
# plik: calkowite15gr.sh
#./calkowite15gr.sh 15 27 1000 1
 
n=$1
k=$2
repf=$3
rep=$4

echo czas: $(date)  
 
for (( res=0; res < $rep ; res+=1 ))
do 
 echo "time python3 GreedyRandomized.py $repf $k $n 1 2>/dev/null | ./sito5 | tee -a wynik15.txt"
 echo "./calkowite15gr.sh $repf $k $n" > ktz2025_todo15.sh
 time  python3 GreedyRandomized.py $repf $k $n 1 2>/dev/null | ./sito5 | tee -a wynik15.txt
done 
 
echo czas: $(date) 
echo "# wszystko zrobione " > ktz2025_todo15.sh
