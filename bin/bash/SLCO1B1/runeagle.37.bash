SAMPLE=$1
VCF=$2

tabix $VCF -R ~/misc/PhasingAstrolabe-0.1/bin/gene/SLCO1B1/tabixregions.txt -h > ~/misc/PhasingAstrolabeOutput/$SAMPLE.chr12.vcf

bcftools norm -d any ~/misc/PhasingAstrolabeOutput/$SAMPLE.chr12.vcf|~/misc/bcftools-1.6/bcftools view -a|~/misc/bcftools-1.6/bcftools view -i 'ALT!="."' -O z -o ~/misc/PhasingAstrolabeOutput/$SAMPLE.bcftools.vcf.gz
tabix ~/misc/PhasingAstrolabeOutput/$SAMPLE.bcftools.vcf.gz

~/misc/Eagle_v2.4/eagle --vcfRef ~/misc/PhasingAstrolabe-0.1/bin/gene/SLCO1B1/slco1b1.pharmvarregions.ref.vcf.gz --vcfTarget ~/misc/PhasingAstrolabeOutput/$SAMPLE.bcftools.vcf.gz  --geneticMapFile ~/misc/Eagle_v2.4/tables/genetic_map_hg19_withX.txt.gz --outPrefix ~/misc/PhasingAstrolabeOutput/$SAMPLE.phased --bpStart 21282128 --bpEnd 21394730 --chrom 12 --allowRefAltSwap --noImpMissing

bgzip -d ~/misc/PhasingAstrolabeOutput/$SAMPLE.phased.vcf.gz
#/software/htslib/current/bin/tabix ~/misc/PhasingAstrolabeOutput/$SAMPLE.phased.vcf.gz R ~/misc/PhasingAstrolabe-0.1/bin/gene/SLCO1B1/tabixregions.txt -h > ~/misc/PhasingAstrolabeOutput/$SAMPLE.phased.filtered.vcf

python ~/misc/PhasingAstrolabe-0.1/bin/python/PhasingAstrolabe.py -vcf ~/misc/PhasingAstrolabeOutput/$SAMPLE.phased.vcf -out ~/misc/PhasingAstrolabeOutput/$SAMPLE.haplotype -loc ~/misc/PhasingAstrolabe-0.1/bin/gene/SLCO1B1/locationData.37.tsv

