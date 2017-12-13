import parsevcf as pv
import argparse as ag
import haplotypecaller as hc
import outputhaplotype as oh

def main():
    parser = ag.ArgumentParser(description ='List of arguments')
    parser.add_argument('-vcf','--vcffilepath',dest='vcf',required=True)
    args = parser.parse_args()
    #print("File: " + args.vcf)
    
    vcfparse = pv.parsevcf()
    vcfparse.readvcf(args.vcf)
    #print(vcfparse.hap1)
    #print(vcfparse.hap2)
    #print(vcfparse.sample)
    call = hc.haplotypecaller('SLCO1B1')
    call.buildhaplotype(vcfparse.get_hap1(),vcfparse.get_hap2())
    out = oh.output()
    regions = out.loadregions()
    rb1 = out.buildregionshap1(regions,call)
    rb2 = out.buildregionshap2(regions,call)
    out.tofile(rb1,rb2,call,vcfparse.sample)
if __name__ == "__main__":main()

