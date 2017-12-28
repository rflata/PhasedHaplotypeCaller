vcf=$1
Sample=$2

java -jar conform-gt.jar gt=$1 chrom=12:21282128-21394730 ref=chr12.ref.vcf.gz match=POS out=$2.conform
java -jar beagle.08Jun17.d8b.jar gt=$2.conform.vcf.gz ref=chr12.ref.vcf.gz map=plink.chr12.GRCh37.map out=$2.phased niterations=10 chrom=12:21282128-21394730 impute=false

python PhasingParser.py $2.phased.vcf.gz