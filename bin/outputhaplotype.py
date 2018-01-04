from collections import defaultdict

class output:
    
    def __init__(self):
        pass
    def loadregions(self):
        self.regions = {}
        with open('locationData.tsv') as locationData:
            for line in locationData:
                if '##REGION' in line:
                    line = line.split('=')
                    line = line[1].split(':')
                    line = line[1].split(';')
                    #print(line[0])
                    self.regions[line[1]] = line[0].split('-')
        #for key, value in regions.items():
            #print(key,value)
        return self.regions

    def buildregionshap1(self,regions,call):
        #print(self.sample)
        #print("Hap1 Shared")
        self.call = call
        self.regionsbuilder = defaultdict(list)
        for hap, variant in self.call.hap1call.items():
            #print(hap)
            #print(variant)
            for loc in variant:
                for key,value in regions.items():
                    location = loc.split('~')
                    if int(location[1]) >= int(value[0]) and int(location[1]) <= int(value[1]):
                        self.regionsbuilder[key.rstrip()].append(loc)
            
        #for key, value in self.regionsbuilder.items():
            #print(key,value)
        return self.regionsbuilder

    def buildregionshap2(self,regions,call):
        #print(self.sample)
        #print("Hap1 Shared")
        self.call = call
        self.regionsbuilderhap2 = defaultdict(list)
        for hap, variant in self.call.hap2call.items():
            #print(hap)
            for loc in variant:
                for key,value in regions.items():
                    location = loc.split('~')
                    if int(location[1]) >= int(value[0]) and int(location[1]) <= int(value[1]):
                        self.regionsbuilderhap2[key.rstrip()].append(loc)
        #for key, value in self.regionsbuilderhap2.items():
            #print(key,value)
        return self.regionsbuilderhap2

    def tofile(self,rb1,rb2,call,sample,cwd,out,regions):
        self.call = call
        self.sample = sample
        with open(out + '.txt','w') as output:
            output.write(self.sample.rstrip() + '\n')
            output.write('Hap1: ')
            i = 0
            for key in self.call.hap1call.keys():
                output.write(key)
                if i < len(self.call.hap1call) -1 and len(self.call.hap1call) > 1:
                    output.write(' or ')
                else:
                    output.write('\n')
                i = i + 1
            
            output.write('Hap2: ')
            i = 0
            for key in self.call.hap2call.keys():
                output.write(key)
                if i < len(self.call.hap2call) -1 and len(self.call.hap2call) > 1:
                    output.write(' or ')
                else:
                    output.write('\n')
                i = i + 1    
            #output.write('Hap2: ')
            #i = 0            
            #for key in self.call.hap2call.keys():
                #output.write(key)
                #if i < len(self.call.hap2call) and len(self.call.hap2call) > 1:
                    #output.write(' or ')
                #i = i + 1
                #output.write('\n')
            output.write('\n' + '--------------------------------------------------------------------------------------------------------------' + '\n')
            output.write('ADDITIONAL INFO' + '\n')
            output.write('--------------------------------------------------------------------------------------------------------------' + '\n')
            for hap, variant in self.call.hap1call.items():
                output.write(hap + '\t' + 'Percent Match: ' + str(call.percentmatchhap1[hap]) + '\t' + 'Variants in Definition: ' + str(len(variant)) + '\n')
                output.write('Variants in Definitions' + '\n')
                output.write('Total: ')
                output.write(','.join(variant))
                output.write('\n')
                #for key, value in rb1.items():
                    #output.write(key + '\n')
                    #print(value)
                    #output.write(','.join(value) + '\n')
                #self.regionsbuilder = defaultdict(list)
                #print(variant)
                for loc in variant:
                    self.regionsbuilder = defaultdict(list)
                    for key,value in regions.items():
                        location = loc.split('~')
                        if int(location[1]) >= int(value[0]) and int(location[1]) <= int(value[1]):
                            self.regionsbuilder[key.rstrip()].append(loc)
                    for key, value in self.regionsbuilder.items():
                        output.write(key + '\n')
                        output.write(','.join(value) + '\n')
                
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
            
            #for key, values in self.call.difhap1.items():
                #print(key)
                #output.write('Variants in Sample Only' + '\n')
                #output.write('Total: ')
                #for x in values:
                    #total = ','.join(values)
                #output.write(total + '\n')
            output.write('\n')
            for hap, variant in self.call.hap2call.items():
                output.write(hap + '\t' + 'Percent Match: ' + str(call.percentmatchhap2[hap]) + '\t' + 'Variants in Definition: ' + str(len(variant)) + '\n')
                output.write('Variants in Definitions' + '\n')
                output.write('Total: ')
                output.write(','.join(variant))
                output.write('\n')
                #for key, value in rb1.items():
                    #output.write(key + '\n')
                    #print(value)
                    #output.write(','.join(value) + '\n')
                #self.regionsbuilder = defaultdict(list)
                #print(variant)
                for loc in variant:
                    self.regionsbuilder = defaultdict(list)
                    for key,value in regions.items():
                        location = loc.split('~')
                        if int(location[1]) >= int(value[0]) and int(location[1]) <= int(value[1]):
                            self.regionsbuilder[key.rstrip()].append(loc)
                    for key, value in self.regionsbuilder.items():
                        output.write(key + '\n')
                        output.write(','.join(value) + '\n')
                
                dif = self.call.difhap2[hap]
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
            print('done')           
            #for hap, variant in self.call.hap2call.items():
                #output.write('\n' + hap + '\n')
                #output.write('Variants in Definitions' + '\n')
                #output.write('Total: ')
                
                #for x in variant:
                    #total = ','.join(variant)
                #output.write(total + '\n')
                
                #for key, value in rb2.items():
                    #output.write(key + '\n')
                    #output.write(','.join(value) + '\n')
                
                #for loc in variant:
                    #self.regionsbuilder = defaultdict(list)
                    #for key,value in regions.items():
                        #location = loc.split('~')
                        #if int(location[1]) >= int(value[0]) and int(location[1]) <= int(value[1]):
                            #self.regionsbuilder[key.rstrip()].append(loc)
                    #for key, value in self.regionsbuilder.items():
                        #output.write(key + '\n')
                        #output.write(','.join(value) + '\n')
                
                #dif = self.call.difhap2[hap]
                #output.write('Variants in Sample Only' + '\n')
                #output.write('Total: ')
                #output.write(','.join(dif))
                #output.write('\n')

                #for loc in dif:
                    #self.regionsbuilder = defaultdict(list)
                    #for key,value in regions.items():
                        #location = loc.split('~')
                        #if int(location[1]) >= int(value[0]) and int(location[1]) <= int(value[1]):
                            #self.regionsbuilder[key.rstrip()].append(loc)
                    #for key, value in self.regionsbuilder.items():
                        #output.write(key + '\n')
                        #output.write(','.join(value) + '\n')
            #for values in self.call.difhap2.values():
                #output.write('Variants in Sample Only' + '\n')
                #output.write('Total: ')
                #for x in values:
                    #total = ','.join(values)
                #output.write(total + '\n')             