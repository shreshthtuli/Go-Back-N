#!/bin/bash


if [ $1 -eq 0 ]
then
	time python3 host.py 0 $2 Programming\ Assignment\ 2.pdf a.txt $3
else
	time python3 host.py 1 $2 Programming\ Assignment\ 2.pdf b.txt $3
fi
