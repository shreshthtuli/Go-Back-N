#!/bin/bash


if [ $1 -eq 0 ]
then
	echo time python3 host.py 0 $2 photo.png a.txt
else
	echo time python3 host.py 1 $2 photo.png b.txt
fi
