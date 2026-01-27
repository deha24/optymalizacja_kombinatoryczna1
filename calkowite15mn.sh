#!/bin/bash
# KTZ 2025 
# plik: calkowite15.sh
#./calkowite15.sh 15 21 $((2**31)) 0 
 
n=$1
e=$2
rep = $3
 
echo czas: $(date)  
 
for (( res=0; res < $rep ; res+=1 ))
do 
 echo "time minizinc --solver gecode /mnt/c/Dawid/Desktop/zajecia/Semestr_3/optymalizacja/greedy.mzn $n $e $rep 2>/dev/null | ./sito5 1 | tee -a wynik15.txt"
 echo "./calkowite15.sh $n $e $rep" > ktz2025_todo15.sh
 time minizinc --solver gecode /mnt/c/Dawid/Desktop/zajecia/Semestr_3/optymalizacja/greedy.mzn $n $e $rep 2>/dev/null | ./sito5 1 | tee -a wynik15.txt
done 
 
echo czas: $(date) 
echo "# wszystko zrobione " > ktz2025_todo15.sh
