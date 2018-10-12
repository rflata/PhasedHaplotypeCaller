SAMPLE=$1
VCF=$2

/software/htslib/current/bin/tabix $VCF 6:18128311-18155165 -h > ~/misc/PhasingAstrolabeOutput/TPMT/$SAMPLE.chr6.vcf

~/misc/bcftools-1.6/bcftools norm -d any ~/misc/PhasingAstrolabeOutput/TPMT/$SAMPLE.chr6.vcf|~/misc/bcftools-1.6/bcftools view -a|~/misc/bcftools-1.6/bcftools view -i 'ALT!="."' -O z -o ~/misc/PhasingAstrolabeOutput/TPMT/$SAMPLE.bcftools.vcf.gz
/software/htslib/current/bin/tabix ~/misc/PhasingAstrolabeOutput/TPMT/$SAMPLE.bcftools.vcf.gz

~/misc/Eagle_v2.4/eagle --vcfRef ~/misc/PhasingAstrolabe-0.1/bin/gene/TPMT/tpmt.reference.vcf.gz --vcfTarget ~/misc/PhasingAstrolabeOutput/TPMT/$SAMPLE.bcftools.vcf.gz  --geneticMapFile ~/misc/Eagle_v2.4/tables/genetic_map_hg19_withX.txt.gz --outPrefix ~/misc/PhasingAstrolabeOutput/TPMT/$SAMPLE.phased --bpStart 18128311 --bpEnd 18155165 --chrom 6 --allowRefAltSwap --noImpMissing --outputUnphased

/software/htslib/current/bin/tabix ~/misc/PhasingAstrolabeOutput/TPMT/$SAMPLE.phased.vcf.gz
/software/htslib/current/bin/tabix ~/misc/PhasingAstrolabeOutput/TPMT/$SAMPLE.phased.vcf.gz -R ~/misc/PhasingAstrolabe-0.1/bin/gene/TPMT/tabixregions.txt -h > ~/misc/PhasingAstrolabeOutput/TPMT/$SAMPLE.phased.filtered.vcf

/software/python/Python-3.6.2/bin/python3.6 ~/misc/PhasingAstrolabe-0.1/bin/python/PhasingAstrolabe.py -vcf ~/misc/PhasingAstrolabeOutput/TPMT/$SAMPLE.phased.filtered.vcf -out ~/misc/PhasingAstrolabeOutput/TPMT/$SAMPLE.haplotype -loc ~/misc/PhasingAstrolabe-0.1/bin/gene/TPMT/locationData.tsv

