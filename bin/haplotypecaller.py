"""
HaployperCaller
Author: Ryan Lata
Primary computational class of the alorgithm, compares the variants pulled from
    phased VCF to the predefined haplotypes in the locationData file
"""

import numpy as np

class haplotypecaller:
    #Haplotypecaller class contructor
    def __init__(self, gene):
        #Setting the default call to *1 allele
        self.callhaplotypehap1 = gene + '*1'
        self.callhaplotypehap2 = gene + '*1'

        self.hap1call = {}
        self.hap1call[self.callhaplotypehap1] = []
        self.hap2call = {}
        self.hap2call[self.callhaplotypehap2] = []

        self.percentmatchhap1 = {}
        self.percentmatchhap1[self.callhaplotypehap1] = 0
        self.percentmatchhap2 = {}
        self.percentmatchhap2[self.callhaplotypehap2] = 0

        self.difhap1 = {}
        self.difhap2 = {}

        self.consensushap1 = {}
        self.consensushap1[self.callhaplotypehap1] = []
        self.consensushap2 = {}
        self.consensushap2[self.callhaplotypehap2] = []
    #Function to build haplotype for each chromosome from phased VCF.
    #Logic:
        # 1. Check if the length of the inputted lists are at least 1
        # 2. If intersection length for the definition is greater than current haplotype call,
            #clear the haplotype call, and set it to new value
        # 3. If the percent match for definition is greater than current haplotype call,
            #and the intersection length is equal or greater than the current haplotype call
            #clear, and set it the current value
        # 4. If the percent match, and intersect are equal there is not consensus in the call,
            #append current value to dictionary do not clear the stored value
    def buildhaplotype(self, hap1, hap2):
        self.difhap1[self.callhaplotypehap1] = hap1
        self.difhap2[self.callhaplotypehap2] = hap2
        with open('locationData.tsv') as locationData:
            #Build Haplotype 1
            if len(hap1) > 0: #Conditional for if there are no variants in the regions
                for line in locationData:
                    if '#' not in line:
                        locationsplit = line.split('\t')
                        snps = locationsplit[1].split(',')
                        #Using intersect1d function from numpy
                        intersecthap1 = np.intersect1d(hap1, snps)
                        #Attempted change in percentmatch calculation to adjust for
                            #the length of the haplotype in the locationData file
                        #May not be the best way to do this, but
                            #haven't seen any issues yet
                        percentmatchhap1temp = (len(intersecthap1)/len(hap1)) * (len(intersecthap1)/len(snps))

                        if len(intersecthap1) > len(self.hap1call[self.callhaplotypehap1]):
                            self.hap1call.clear()
                            self.hap1call[locationsplit[0]] = intersecthap1.tolist()
                            self.callhaplotypehap1 = locationsplit[0]
                            self.percentmatchhap1.clear()
                            self.percentmatchhap1[self.callhaplotypehap1] = percentmatchhap1temp
                            self.difhap1.clear()
                            self.difhap1[self.callhaplotypehap1] = np.setdiff1d(hap1, snps).tolist()
                            self.consensushap1.clear()
                            self.consensushap1[locationsplit[0]] = snps

                        if percentmatchhap1temp > self.percentmatchhap1[self.callhaplotypehap1] and len(intersecthap1) >= len(self.hap1call[self.callhaplotypehap1]):
                            self.hap1call.clear()
                            self.hap1call[locationsplit[0]] = intersecthap1.tolist()
                            self.callhaplotypehap1 = locationsplit[0]
                            self.percentmatchhap1.clear()
                            self.difhap1.clear()
                            self.difhap1[self.callhaplotypehap1] = np.setdiff1d(hap1, snps).tolist()
                            self.consensushap1.clear()
                            self.consensushap1[locationsplit[0]] = snps

                        elif percentmatchhap1temp == self.percentmatchhap1[self.callhaplotypehap1] and len(intersecthap1) == len(self.hap1call[self.callhaplotypehap1]) and len(intersecthap1) != 0:
                            self.hap1call[locationsplit[0]] = intersecthap1.tolist()
                            self.percentmatchhap1[locationsplit[0]] = percentmatchhap1temp
                            self.difhap1[locationsplit[0]] = np.setdiff1d(hap1, snps).tolist()
                            self.consensushap1[locationsplit[0]] = snps

        #Build Haploype 2, same logic applies as haplotype 1
        with open('locationData.tsv') as locationData:
            if len(hap2) > 0: #Conditional for if there are no variants in the regions
                for line in locationData:
                    #print(line)
                    if '#' not in line:
                        locationsplit = line.split('\t')
                        snps = locationsplit[1].split(',')

                        intersecthap2 = np.intersect1d(hap2, snps)
                        percentmatchhap2temp = (len(intersecthap2)/len(hap2)) * (len(intersecthap2)/len(snps))

                        if len(intersecthap2) > len(self.hap2call[self.callhaplotypehap2]):
                            self.hap2call.clear()
                            self.hap2call[locationsplit[0]] = intersecthap2.tolist()
                            self.callhaplotypehap2 = locationsplit[0]
                            self.percentmatchhap2.clear()
                            self.percentmatchhap2[locationsplit[0]] = percentmatchhap2temp
                            self.difhap2.clear()
                            self.difhap2[locationsplit[0]] = np.setdiff1d(hap2, snps).tolist()
                            self.consensushap2.clear()
                            self.consensushap2[locationsplit[0]] = snps

                        if percentmatchhap2temp > self.percentmatchhap2[self.callhaplotypehap2] and len(intersecthap2) >= len(self.hap2call[self.callhaplotypehap2]):
                            self.hap2call.clear()
                            self.hap2call[locationsplit[0]] = intersecthap2.tolist()
                            self.callhaplotypehap2 = locationsplit[0]
                            self.percentmatchhap2.clear()
                            self.percentmatchhap2[locationsplit[0]] = percentmatchhap2temp
                            self.difhap2.clear()
                            self.difhap2[locationsplit[0]] = np.setdiff1d(hap2, snps).tolist()
                            self.consensushap2.clear()
                            self.consensushap2[locationsplit[0]] = snps

                        elif percentmatchhap2temp == self.percentmatchhap2[self.callhaplotypehap2] and len(intersecthap2) == len(self.hap2call[self.callhaplotypehap2]) and len(intersecthap2) != 0:
                            self.hap2call[locationsplit[0]] = intersecthap2.tolist()
                            self.percentmatchhap2[locationsplit[0]] = percentmatchhap2temp
                            self.difhap2[locationsplit[0]] = np.setdiff1d(hap2,snps).tolist()
                            self.consensushap2[locationsplit[0]] = snps
