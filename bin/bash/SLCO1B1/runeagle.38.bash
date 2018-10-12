SAMPLE=$1
VCF=$2

/software/htslib/current/bin/tabix $VCF -R ~/misc/PhasingAstrolabe-0.1/bin/gene/SLCO1B1/tabixregions.38.txt -h > ~/misc/PhasingAstrolabeOutput/$SAMPLE.chr12.vcf
sed -i 's/chr12/12/g' ~/misc/PhasingAstrolabeOutput/$SAMPLE.chr12.vcf
~/misc/bcftools-1.6/bcftools norm -d any ~/misc/PhasingAstrolabeOutput/$SAMPLE.chr12.vcf|~/misc/bcftools-1.6/bcftools view -a|~/misc/bcftools-1.6/bcftools view -i 'ALT!="."' -O z -o ~/misc/PhasingAstrolabeOutput/$SAMPLE.bcftools.vcf.gz
/software/htslib/current/bin/tabix ~/misc/PhasingAstrolabeOutput/$SAMPLE.bcftools.vcf.gz

~/misc/Eagle_v2.4/eagle --vcfRef ~/SLCO1B1/ALL.chr12_GRCh38.genotypes.20170504.vcf.gz --vcfTarget ~/misc/PhasingAstrolabeOutput/$SAMPLE.bcftools.vcf.gz  --geneticMapFile ~/misc/Eagle_v2.4/tables/genetic_map_hg38_withX.txt.gz --outPrefix ~/misc/PhasingAstrolabeOutput/$SAMPLE.phased --bpStart 21131194 --bpEnd 21239796 --chrom 12 --allowRefAltSwap --noImpMissing

/software/htslib/current/bin/bgzip -d ~/misc/PhasingAstrolabeOutput/$SAMPLE.phased.vcf.gz
#/software/htslib/current/bin/tabix ~/misc/PhasingAstrolabeOutput/$SAMPLE.phased.vcf.gz R ~/misc/PhasingAstrolabe-0.1/bin/gene/SLCO1B1/tabixregions.txt -h > ~/misc/PhasingAstrolabeOutput/$SAMPLE.phased.filtered.vcf

/software/python/Python-3.6.2/bin/python3.6 ~/misc/PhasingAstrolabe-0.1/bin/python/PhasingAstrolabe.py -vcf ~/misc/PhasingAstrolabeOutput/$SAMPLE.phased.vcf -out ~/misc/PhasingAstrolabeOutput/$SAMPLE.haplotype -loc ~/misc/PhasingAstrolabe-0.1/bin/gene/SLCO1B1/locationData.38.tsv

