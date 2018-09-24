#!/bin/bash


if [ $1 -eq 0 ]
then
	time python3 host.py 0 $2 README.md a.txt $3
else
	time python3 host.py 1 $2 README.md b.txt $3
fi
