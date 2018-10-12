#! /bin/bash

while IFS=$'\t' read sample v; do
	echo $sample
	/home/rflata/misc/PhasingAstrolabe-0.1/bin/runeagle.bash $sample $v
done < /home/rflata/sample.locations/get.rm.idt.txt
