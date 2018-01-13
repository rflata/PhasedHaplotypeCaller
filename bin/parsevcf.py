class parsevcf:
    
    def __init__(self):
        self.hap1 = []
        self.hap2 = []
        self.sample = ''
    #Setter and getters for encapsulation of parsevcf variables (may remove at somepoint)
    def set_hap1(self, x):
        self.hap1.append(x)
    
    def set_hap2(self,x):
        self.hap2.append(x)
    
    def get_hap1(self):
        return self.hap1 
    
    def get_hap2(self):
        return self.hap2
    #Function to read the user inputted VCF. Will only store phased variants in memory.
    def readvcf(self,vcf):
        with open(vcf) as vcf:
            for line in vcf:
                #Getting the sample name from the VCF (may fail if VCF header is not inputted as expected)
                if '#CHROM' in line:
                    sampleline = line.split('\t')
                    self.sample = sampleline[9]
                #Looking at each position in the VCF file and storing variants sites from each chromosome in dictionaries.
                if "#" not in line:
                    split = line.split('\t')
                    ref = split[3]
                    alt = split[4]
                    alt = alt.split(',')
                    variant = split[9]
                    variantsplit = variant.split('|')
                    hap1temp = split[0] + '~' + split[1] + '~'+ split[1] + '~' + alt[int(variantsplit[0])-1]
                    if int(variantsplit[0]) != 0:
                        self.set_hap1(hap1temp)
                    hap2temp = split[0] + '~' + split[1] + '~'+ split[1] + '~' + alt[int(variantsplit[1])-1].strip('\n')
                    if int(variantsplit[1]) != 0:
                        self.set_hap2(hap2temp)