class parsevcf:
    
    def __init__(self):
        self.hap1 = []
        self.hap2 = []
        self.sample = ''
    
    def set_hap1(self, x):
        self.hap1.append(x)
    
    def set_hap2(self,x):
        self.hap2.append(x)
    
    def get_hap1(self):
        return self.hap1 
    
    def get_hap2(self):
        return self.hap2

    def readvcf(self,vcf):
        with open(vcf) as vcf:
            for line in vcf:
                #print(line)
                if '#CHROM' in line:
                    sampleline = line.split('\t')
                    self.sample = sampleline[9]
                if "#" not in line:
                    split = line.split('\t')
                    ref = split[3]
                    alt = split[4]
                    alt = alt.split(',')
                    variant = split[9]
                    variantsplit = variant.split('|')
                    hap1temp = split[0] + '~' + split[1] + '~'+ split[1] + '~' + alt[int(variantsplit[0])-1]
                    if variantsplit[0] != '0':
                        self.set_hap1(hap1temp)
                    hap2temp = split[0] + '~' + split[1] + '~'+ split[1] + '~' + alt[int(variantsplit[1])-1].strip('\n')
                    if variantsplit[1] != '0':
                        self.set_hap2(hap2temp)