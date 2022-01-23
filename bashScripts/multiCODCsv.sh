#!/bin/bash

inCODDir="$1"

fmtFile="$2"

outCsv="$3"

threadN="$4"

defaultThreadN=4

echo "inCODDir=$inCODDir fmtFile=$fmtFile outCsv=$outCsv threadN=$threadN"

[ ! $inCODDir ] && echo "error: inCODDir cannot be empty" && exit 4

[ ! $fmtFile ] && echo "error: fmtFile cannot be empty" && exit 5

[ ! $outCsv ] && echo "error: outCsv cannot be empty" && exit 6

[[ ! "$outCsv" == *.csv ]] && echo "error: outCsv has to end with .csv" &&\
    exit 7


[ ! -d $inCODDir ] &&\
    echo "error: $inCODDir is not a directory" && exit 1

for e in $(seq 1 9)
do
    [ ! -d $inCODDir/$e ] &&\
	echo "error: $inCODDir/$e doesn't exist" &&\
	echo "are you sure it's the path for the COD database?" &&\
	exit 2
done

[ ! -f $fmtFile ] &&\
    echo "error: $fmtFile does not exist" && exit 3

case $threadN in
    ('')
	echo "using default threadN value of $defaultThreadN"; threadN=$defaultThreadN ;;
    (*[!0-9]*)
	echo "error: threadN is not a number" && exit 8;;
    (0*)
	echo "error: threadN cannot be zero" && exit 9;;
    (*)
	echo "ok2go";;
esac

#Testing this
N=$threadN
(
    for e in $(seq 1 9)
    do
	for ee in $inCODDir/$e/*
	do
	    outCsv="$e""_""$(basename $ee)"".csv"
	    echo outCsv $outCsv
	    cif2Csv $ee $fmtFile $outCsv &&\
		echo "Finished $outCsv" &
	    ((i=i%N)); ((i++==0)) && wait
	done
    done
    wait
)

cat *_*.csv > $outCsv
rm *_*.csv

exit 0
