SAMPLE=$1
VCF=$2
/software/htslib/current/bin/tabix $VCF -R tabixregiontest.txt -h > /home/rflata/misc/PhasingAstrolabeOutput/$SAMPLE.chr12.vcf
sed -i -e "s/$SAMPLE/$SAMPLE.phased/g" /home/rflata/misc/PhasingAstrolabeOutput/$SAMPLE.chr12.vcf
~/misc/bcftools-1.6/bcftools norm -d any /home/rflata/misc/PhasingAstrolabeOutput/$SAMPLE.chr12.vcf|~/misc/bcftools-1.6/bcftools view -a|~/misc/bcftools-1.6/bcftools view -i 'ALT!="."' -o /home/rflata/misc/PhasingAstrolabeOutput/$SAMPLE.bcftools.vcf
#/home/rflata/misc/java8/bin/java -cp ./ -jar /home/rflata/misc/PhasingAstrolabe-0.1/Beagle/conform-gt.jar gt=/home/rflata/misc/PhasingAstrolabeOutput/$SAMPLE.chr12.vcf chrom=12:21282128-21394730 ref=/home/rflata/misc/PhasingAstrolabe-0.1/Beagle/slco1b1.ref.vcf.gz match=POS out=/home/rflata/misc/PhasingAstrolabeOutput/$SAMPLE.conform
/home/rflata/misc/java8/bin/java -cp ./ -jar ~/misc/PhasingAstrolabe-0.1/Beagle/beagle.08Jun17.d8b.jar gt=/home/rflata/misc/PhasingAstrolabeOutput/$SAMPLE.bcftools.vcf ref=/home/rflata/misc/PhasingAstrolabe-0.1/Beagle/slco1b1.ref.alt.vcf map=/home/rflata/misc/PhasingAstrolabe-0.1/Beagle/plink.chr12.GRCh37.map out=/home/rflata/misc/PhasingAstrolabeOutput/$SAMPLE.phased chrom=12:21282128-21394730 impute=false
/software/htslib/current/bin/bgzip -d /home/rflata/misc/PhasingAstrolabeOutput/$SAMPLE.phased.vcf.gz
/software/python/Python-3.6.2/bin/python3.6 /home/rflata/misc/PhasingAstrolabe-0.1/bin/PhasingAstrolabe.py -vcf /home/rflata/misc/PhasingAstrolabeOutput/$SAMPLE.phased.vcf -out /home/rflata/misc/PhasingAstrolabeOutput/$SAMPLE.haplotype