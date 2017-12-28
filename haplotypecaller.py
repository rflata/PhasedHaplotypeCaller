import numpy as np

class haplotypecaller:
    def __init__(self,gene):
        self.callhaplotypehap1 = gene + '*1'
        #print(self.callhaplotypehap1)
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
    def buildhaplotype(self,hap1,hap2):
        self.difhap1[self.callhaplotypehap1] = hap1
        self.difhap2[self.callhaplotypehap2] = hap2
        with open('locationData.tsv') as locationData:    
            for line in locationData:
                if '#' not in line:
                    locationsplit = line.split('\t')
                    snps = locationsplit[1].split(',')
                    
                    intersecthap1 = np.intersect1d(hap1,snps)
                    intersecthap2 = np.intersect1d(hap2,snps)
                    
                    percentmatchhap1temp = (len(intersecthap1)/len(hap1)) * (len(intersecthap1)/len(snps))
                    percentmatchhap2temp = (len(intersecthap2)/len(hap2)) * (len(intersecthap2)/len(snps))
                    
                    if len(intersecthap1) > len(self.hap1call[self.callhaplotypehap1]):
                        #print(locationsplit[0])
                        self.hap1call.clear()
                        self.hap1call[locationsplit[0]] = intersecthap1.tolist()
                        self.callhaplotypehap1 = locationsplit[0]
                        self.percentmatchhap1.clear()
                        #print(percentmatchhap1temp)
                        self.percentmatchhap1[self.callhaplotypehap1] = percentmatchhap1temp
                        #print(self.percentmatchhap1)
                        self.difhap1.clear()
                        self.difhap1[self.callhaplotypehap1] = np.setdiff1d(hap1,snps).tolist()
                        #print(self.callhaplotypehap1)
                        #for key, value in self.hap1call.items():
                            #print('Both Greater')
                            #print(key,value)
                    if percentmatchhap1temp > self.percentmatchhap1[self.callhaplotypehap1] and len(intersecthap1) >= len(self.hap1call[self.callhaplotypehap1]):
                        #print(locationsplit[0])
                        self.hap1call.clear()
                        self.hap1call[locationsplit[0]] = intersecthap1.tolist()
                        self.callhaplotypehap1 = locationsplit[0]
                        self.percentmatchhap1.clear()
                        #print(percentmatchhap1temp)
                        self.percentmatchhap1[self.callhaplotypehap1] = percentmatchhap1temp
                        #print(self.percentmatchhap1)
                        self.difhap1.clear()
                        self.difhap1[self.callhaplotypehap1] = np.setdiff1d(hap1,snps).tolist()                    
                    elif percentmatchhap1temp == self.percentmatchhap1[self.callhaplotypehap1] and len(intersecthap1) == len(self.hap1call[self.callhaplotypehap1]):
                        self.hap1call[locationsplit[0]] = intersecthap1.tolist()
                        self.percentmatchhap1[locationsplit[0]] = percentmatchhap1temp
                        self.difhap1[locationsplit[0]] = np.setdiff1d(hap1,snps).tolist()
                        #print('Both Equal')
                        #for key, value in self.hap1call.items():
                            #print(key,value)
                    if len(intersecthap2) > len(self.hap2call[self.callhaplotypehap2]):
                        self.hap2call.clear()
                        self.hap2call[locationsplit[0]] = intersecthap2.tolist()
                        self.callhaplotypehap2 = locationsplit[0]
                        self.percentmatchhap2.clear()
                        self.percentmatchhap2[locationsplit[0]] = percentmatchhap2temp
                        self.difhap2.clear()
                        self.difhap2[locationsplit[0]] = np.setdiff1d(hap2,snps).tolist()
                        #print(self.callhaplotypehap1)
                        #for key, value in self.hap1call.items():
                            #print('Both Greater')
                            #print(key,value)
                    
                    if percentmatchhap2temp > self.percentmatchhap2[self.callhaplotypehap2] and len(intersecthap2) >= len(self.hap2call[self.callhaplotypehap2]):
                        self.hap2call.clear()
                        self.hap2call[locationsplit[0]] = intersecthap2.tolist()
                        self.callhaplotypehap2 = locationsplit[0]
                        self.percentmatchhap2.clear()
                        self.percentmatchhap2[locationsplit[0]] = percentmatchhap2temp
                        self.difhap2.clear()
                        self.difhap2[locationsplit[0]] = np.setdiff1d(hap2,snps).tolist()
                        #print(self.callhaplotypehap1)
                        #for key, value in self.hap1call.items():
                            #print('Both Greater')
                            #print(key,value)
                    elif percentmatchhap2temp == self.percentmatchhap2[self.callhaplotypehap2] and len(intersecthap2) == len(self.hap2call[self.callhaplotypehap2]):
                        self.hap2call[locationsplit[0]] = intersecthap2.tolist()
                        self.percentmatchhap2[locationsplit[0]] = percentmatchhap2temp
                        self.difhap2[locationsplit[0]] = np.setdiff1d(hap2,snps).tolist()
                        #print('Both Equal')
                        #for key, value in self.hap1call.items():
                            #print(key,value)