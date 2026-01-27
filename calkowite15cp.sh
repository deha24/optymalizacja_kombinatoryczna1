#!/bin/bash
# KTZ 2025 
# plik: calkowite15cp.sh
#./calkowite15.sh 15 27 1000 
 
n=$1
e=$2
rep=$3

echo czas: $(date)  
 
for (( res=0; res < $rep ; res+=1 ))
do 
 echo "time python3 gengnk.py $n $e 1 2>/dev/null | ./sito5 | tee -a wynik8.txt"
 echo "./calkowite15cp.sh $n $e $rep" > ktz2025_todo15.sh
 time  python3 gengnk.py $n $e 1 2>/dev/null | ./sito5 | tee -a wynik8.txt
done 
 
echo czas: $(date) 
echo "# wszystko zrobione " > ktz2025_todo15.sh
