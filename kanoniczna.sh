#!/bin/bash
# plik: kanoniczna.sh
#./kanoniczna.sh [[plik_zrodlo]] [[plik_destynacja]]

files=$1
filed=$2

echo czas: $(date)

cat $files | ./labelg | sort | uniq > $filed

echo czas: $(date)
