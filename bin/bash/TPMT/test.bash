#! /bin/bash

while IFS=$'\t' read sample v; do
	~/misc/PhasingAstrolabe-0.1/bin/bash/TPMT/runeagle.bash "$sample" "$v"
done < /home/rflata/sample.locations/Samples.txt
