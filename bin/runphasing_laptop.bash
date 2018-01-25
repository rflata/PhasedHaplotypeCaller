SAMPLE=$1
VCF=$2
tabix $VCF -R tabixregiontest.txt -h > /mnt/d/Test/$SAMPLE.chr12.vcf
sed -i -e "s/$SAMPLE/$SAMPLE.phased/g" /mnt/d/Test/$SAMPLE.chr12.vcf
bcftools norm -d any /mnt/d/Test/$SAMPLE.chr12.vcf|bcftools view -a|bcftools view -i 'ALT!="."' -o /mnt/d/Test/$SAMPLE.bcftools.vcf
#java -jar /mnt/c/Linux/PhasingAstrolabe/beag/conform-gt.jar gt=/mnt/d/Test/$SAMPLE.chr12.vcf chrom=12:21282128-21394730 ref=/mnt/c/Linux/PhasingAstrolabe/beag/slco1b1.ref.vcf.gz match=POS out=/mnt/d/Test/$SAMPLE.conform
java -jar /mnt/c/Linux/PhasingAstrolabe/Beagle/beagle.08Jun17.d8b.jar gt=/mnt/d/Test/$SAMPLE.bcftools.vcf ref=/mnt/c/Linux/PhasingAstrolabe/Beagle/slco1b1.ref.alt.vcf map=/mnt/c/Linux/PhasingAstrolabe/Beagle/plink.chr12.GRCh37.map out=/mnt/d/Test/$SAMPLE.phased chrom=12:21282128-21394730 impute=false niterations=20
bgzip -d /mnt/d/Test/$SAMPLE.phased.vcf.gz
python3.6 PhasingAstrolabe.py -vcf /mnt/d/Test/$SAMPLE.phased.vcf -out /mnt/d/Test/$SAMPLE.haplotype