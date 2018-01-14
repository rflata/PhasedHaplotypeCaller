"""
PhasingAstrolabe
Author: Ryan Lata
Includes the main function for running algorithm
"""

import argparse as ag
import parsevcf as pv
import haplotypecaller as hc
import outputhaplotype as oh

def main():
    #Two Required arugments: VCF File and Output File name/destination
    parser = ag.ArgumentParser(description='List of arguments')
    parser.add_argument('-vcf', '--vcffilepath', dest='vcf', required=True)
    parser.add_argument('-out', '--output', dest='out', required=True)
    parser.add_argument('-type', '--filetype', dest='type',
                        choices=['csv', 'list'],
                        help='Limits the output to csv or list format (Default = both')
    args = parser.parse_args()

    #Calling the parsevcf() constructor
    vcfparse = pv.parsevcf()
    #Pulls variants from VCF file and stores them in two dictionaries
    vcfparse.readvcf(args.vcf)

    #Starting the haplotypecaller which compares the variants
    #obtained from the parsed VCF to the definition file.
    #Currenlty only functional for a single gene, but plan to expand it to multiple
    call = hc.haplotypecaller('SLCO1B1')
    call.buildhaplotype(vcfparse.get_hap1(), vcfparse.get_hap2())
    #Outputting the contstructed haplotypes to file
    out = oh.output()
    regions = out.loadregions()
    #rb1 = out.buildregionshap1(regions,call)
    #rb2 = out.buildregionshap2(regions,call)
    if args.out == 'csv':
        out.tocsv(call, vcfparse.sample, args.out, regions)
    if args.out == 'list':
        out.tolist(call, vcfparse.sample, args.out, regions)
    else:
        out.tocsv(call, vcfparse.sample, args.out, regions)
        out.tolist(call, vcfparse.sample, args.out, regions)
if __name__ == "__main__": main()
