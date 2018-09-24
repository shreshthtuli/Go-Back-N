#!/bin/bash


if [$1 == 0]
then
	echo time python3 host.py 0 $2 photo.png a.txt
elif [$1 == 1]
then
	echo time python3 host.py 1 $2 photo.png b.txt
fi
