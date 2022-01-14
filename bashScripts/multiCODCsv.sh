#!/bin/bash

inCODDir="$1"

fmtFile="$2"

echo "inCODDir=$inCODDir fmtFile=$fmtFile"

[ ! $inCODDir ] && echo "error: inCODDir cannot be empty" && exit 4

[ ! $fmtFile ] && echo "error: fmtFile cannot be empty" && exit 5

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

# N=4
# (
#     for e in $(seq 1 9)
#     do
# 	count=$(cif2Csv $inCODDir/$e -c) &
# 	echo $inCODDir/$e $count
# 	((i=i%N)); ((i++==0)) && wait
#     done
# )

#special directory listing
# N=4
# (
#     for e in $(seq 1 9)
#     do
# 	if [ $e -eq 4 ] || [ $e -eq 7 ] 
# 	then
# 	    for ee in $inCODDir/$e/*
# 	    do
# 		outCsv="$e""_""$(basename $ee)"".csv"
# 		echo outCsv $outCsv
# 		count=$(cif2Csv $ee -c) &&\
# 		    echo $ee $count &
# 		((i=i%N)); ((i++==0)) && wait
# 	    done
# 	else
# 	    outCsv="$e"".csv"
# 	    echo outCsv $outCsv
# 	    count=$(cif2Csv $inCODDir/$e -c) &&\
# 		echo $inCODDir/$e $count &
# 	    ((i=i%N)); ((i++==0)) && wait
# 	fi

#     done
#     wait
# )

#Counting differently
# N=4
# (
#     for e in $(seq 1 9)
#     do
# 	for ee in $inCODDir/$e/*
# 	do
# 	    outCsv="$e""_""$(basename $ee)"".csv"
# 	    echo outCsv $outCsv
# 	    count=$(cif2Csv $ee -c) &&\
# 		echo $(basename $outCsv .csv) $count > $outCsv &&
# 		echo $ee $count &
# 	    ((i=i%N)); ((i++==0)) && wait
# 	done
#     done
#     wait
# )

# cat *_*.csv > total.csv

# rm *_*.csv

#Testing this
N=8
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

cat *_*.csv > total.csv
rm *_*.csv

exit 0
