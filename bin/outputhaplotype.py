#PhasingAstrolabe
#Author: Ryan Lata
#Code to output data into a readable format

from collections import defaultdict

class output:
    def __init__(self):
        pass
    
    #Function to load the defined regions of interest for the gene from the locationData file
    def loadregions(self):
        self.regions = {}
        with open('locationData.tsv') as locationData:
            for line in locationData:
                if '##REGION' in line:
                    line = line.split('=')
                    line = line[1].split(':')
                    line = line[1].split(';')
                    self.regions[line[1]] = line[0].split('-')
        return self.regions
   
    #Deprecated functions
    #def buildregionshap1(self,regions,call):
    #    # print(self.sample)
    #    # print("Hap1 Shared")
    #    self.call = call
    #    self.regionsbuilder = defaultdict(list)
    #    for hap, variant in self.call.hap1call.items():
    #        # print(hap)
    #        # print(variant)
    #        for loc in variant:
    #            for key,value in regions.items():
    #                location = loc.split('~')
    #                if int(location[1]) >= int(value[0]) and int(location[1]) <= int(value[1]):
    #                    self.regionsbuilder[key.rstrip()].append(loc)
    #        
    #    # for key, value in self.regionsbuilder.items():
    #        # print(key,value)
    #    return self.regionsbuilder

    #def buildregionshap2(self,regions,call):
    #    #print(self.sample)
    #    #print("Hap1 Shared")
    #    self.call = call
    #    self.regionsbuilderhap2 = defaultdict(list)
    #    for hap, variant in self.call.hap2call.items():
    #        #print(hap)
    #        for loc in variant:
    #            for key,value in regions.items():
    #                location = loc.split('~')
    #                if int(location[1]) >= int(value[0]) and int(location[1]) <= int(value[1]):
    #                    self.regionsbuilderhap2[key.rstrip()].append(loc)
    #    #for key, value in self.regionsbuilderhap2.items():
    #        #print(key,value)
    #    return self.regionsbuilderhap2

    #Function for outputing data to a file
    def tolist(self,call,sample,out,regions):
        self.call = call
        self.sample = sample
        with open(out + '.txt','w') as output:
            output.write(self.sample.rstrip() + '\n')
            output.write('Hap1: ')
            i = 0
            
            #Poor attempt to add or inbetween calls when no consensus is presence, it works...but likely is a better way
            for key in self.call.hap1call.keys():
                output.write(key)
                if i < len(self.call.hap1call) -1 and len(self.call.hap1call) > 1:
                    output.write(' or ')
                else:
                    output.write('\n')
                i = i + 1
            #Same as above
            output.write('Hap2: ')
            i = 0
            for key in self.call.hap2call.keys():
                output.write(key)
                if i < len(self.call.hap2call) -1 and len(self.call.hap2call) > 1:
                    output.write(' or ')
                else:
                    output.write('\n')
                i = i + 1    
            
            #Some useful additional information to be included with the haplotype calls
            output.write('\n' + '--------------------------------------------------------------------------------------------------------------' + '\n')
            output.write('ADDITIONAL INFO' + '\n')
            output.write('--------------------------------------------------------------------------------------------------------------' + '\n')
            
            for hap, variant in self.call.hap1call.items():
                output.write(hap + '\t' + 'Percent Match: ' + str(call.percentmatchhap1[hap]) + '\t' + 'Variants in Definition: ' + str(len(variant)) + '\n')
                output.write('Variants in Definitions' + '\n')
                output.write('Total: ')
                output.write(','.join(variant))
                output.write('\n')
                
                #Checking the exon location of the variant
                for loc in variant:
                    self.regionsbuilder = defaultdict(list)
                    for key,value in regions.items():
                        location = loc.split('~')
                        if int(location[1]) >= int(value[0]) and int(location[1]) <= int(value[1]):
                            self.regionsbuilder[key.rstrip()].append(loc)
                    for key, value in self.regionsbuilder.items():
                        output.write(key + '\n')
                        output.write(','.join(value) + '\n')
                
                #Outputing variants that are not found in the consensus definition, but are found in the VCR
                dif = self.call.difhap1[hap]
                output.write('Variants in Sample Only' + '\n')
                output.write('Total: ')
                output.write(','.join(dif))
                output.write('\n')

                for loc in dif:
                    self.regionsbuilder = defaultdict(list)
                    for key,value in regions.items():
                        location = loc.split('~')
                        if int(location[1]) >= int(value[0]) and int(location[1]) <= int(value[1]):
                            self.regionsbuilder[key.rstrip()].append(loc)
                    for key, value in self.regionsbuilder.items():
                        output.write(key + '\n')
                        output.write(','.join(value) + '\n')               

            output.write('\n')
            
            for hap, variant in self.call.hap2call.items():
                output.write(hap + '\t' + 'Percent Match: ' + str(call.percentmatchhap2[hap]) + '\t' + 'Variants in Definition: ' + str(len(variant)) + '\n')
                output.write('Variants in Definitions' + '\n')
                #output.write('Total: ')
                #output.write(','.join(variant))
                output.write('\n')
                for loc in variant:
                    self.regionsbuilder = defaultdict(list)
                    for key,value in regions.items():
                        location = loc.split('~')
                        if int(location[1]) >= int(value[0]) and int(location[1]) <= int(value[1]):
                            self.regionsbuilder[key.rstrip()].append(loc)
                    for key, value in self.regionsbuilder.items():
                        output.write(key + '\n')
                        output.write(','.join(value) + '\n')
                output.write('Total: ')
                output.write(','.join(variant))

                dif = self.call.difhap2[hap]
                output.write('Variants in Sample Only' + '\n')
                #output.write('Total: ')
                #output.write(','.join(dif))
                output.write('\n')
                output.write('Total: ')
                output.write(','.join(dif))
                
                for loc in dif:
                    self.regionsbuilder = defaultdict(list)
                    for key,value in regions.items():
                        location = loc.split('~')
                        if int(location[1]) >= int(value[0]) and int(location[1]) <= int(value[1]):
                            self.regionsbuilder[key.rstrip()].append(loc)
                    for key, value in self.regionsbuilder.items():
                        output.write(key + '\n')
                        output.write(','.join(value) + '\n')               
            print('done')           
    #Option to output data as a CSV
    def tocsv(self,call,sample,out,regions):
        self.sample = sample
        self.call = call
        with open(out + '.csv','w') as output:
            output.write(self.sample.rstrip() + '\n')
            
            for key, value in call.consensushap1.items():
                output.write(key + ' Definition' + ',')
                value = sorted(value)
                output.write(','.join(value) + '\n') 

            for hap, variant in self.call.hap1call.items():
                output.write('Hap1 Call,')
                output.write(','.join(variant) + '\n')
                
                dif = self.call.difhap1[hap]
                output.write('Hap1 Sample Only,')
                output.write(','.join(dif) + '\n')
            
            for key, value in call.consensushap2.items():
                output.write(key + ' Definition' + ',')
                value = sorted(value)
                output.write(','.join(value) + '\n') 

            for hap, variant in self.call.hap2call.items():
                output.write('Hap1 Call,')
                output.write(','.join(variant) + '\n')
                
                dif = self.call.difhap2[hap]
                output.write('Hap1 Sample Only,')
                output.write(','.join(dif) + '\n')