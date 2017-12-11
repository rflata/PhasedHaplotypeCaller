import numpy as np
with open('/mnt/d/Linux/SLCO1B1/1000_Genomes_Data/NA07019.phased.vcf') as vcf:
    hap1 = []
    hap2 = []
    for line in vcf:
        if '#CHROM' in line:
            sampleline = line.split('\t')
            sample = sampleline[9]
        if "#" not in line:
            split = line.split('\t')
            ref = split[3]
            alt = split[4]
            alt = alt.split(',')
            variant = split[9]
            variantsplit = variant.split('|')
            hap1temp = split[0] + '~' + split[1] + '~'+ split[1] + '~' + alt[int(variantsplit[0])-1]
            if variantsplit[0] != '0':
                hap1.append(hap1temp)
            hap2temp = split[0] + '~' + split[1] + '~'+ split[1] + '~' + alt[int(variantsplit[1])-1].strip('\n')
            if variantsplit[1] != '0':
                hap2.append(hap2temp)
    print('Hap1 ', hap1)
    print('Hap2 ', hap2)
with open('/mnt/c/Linux/locationData.tsv') as locationData,open('/mnt/c/Linux/Astrolabe.txt','w') as Astrolabe:
    finalpercentmatchhap1 = 0
    finalpercentmatchhap2 = 0
    callhaplotypehap1 = 'SLCO1B1*1'
    callhaplotypehap2 = 'SLCO1B1*1'
    callhap1 = []
    callhap2 = []
    differencehap1 = hap1
    differencehap2 = hap2
    for line in locationData:
        if '#' not in line:
            locationsplit = line.split('\t')
            snps = locationsplit[1].split(',')
            print(snps)
            intersecthap1 = np.intersect1d(hap1,snps)
            print(intersecthap1)
            intersecthap2 = np.intersect1d(hap2,snps).tolist()
            print(intersecthap2)
            differencehap1temp = np.setdiff1d(hap1,snps).tolist()
            differencehap2temp = np.setdiff1d(hap2,snps).tolist()
            calltemphap1 = intersecthap1
            calltemphap2 = intersecthap2

            calltemphaplotypehap1 = locationsplit[0]
            calltemphaplotypehap2 = locationsplit[0]
            percentmatchtemphap1 = (len(calltemphap1)/len(snps))*len(snps)
            if percentmatchtemphap1 > finalpercentmatchhap1:
                callhap1 = calltemphap1
                callhaplotypehap1 = calltemphaplotypehap1
                finalpercentmatchhap1 = percentmatchtemphap1
                differencehap1 = differencehap1temp
            calltemphap2 = intersecthap2
            calltemphaplotypehap2 = locationsplit[0]
            percentmatchtemphap2 = (len(calltemphap2)/len(snps))*len(snps)
            if percentmatchtemphap2 > finalpercentmatchhap2:
                callhap2 = calltemphap2
                callhaplotypehap2 = calltemphaplotypehap2
                finalpercentmatchhap2 = percentmatchtemphap2
                differencehap2 = differencehap2temp
    print('Sample: ',sample)
    print('Haplotype1: ',callhaplotypehap1)
    print('Shared SNPs: ',callhap1)
    print('Percent Match: ',finalpercentmatchhap1)
    print('Sample Only Haplotype1: ',differencehap1)
    print('Haplotye2: ',callhaplotypehap2)
    print('Shared SNPs: ',callhap2)
    print('Percent Match: ',finalpercentmatchhap2)
    print('Sample Only Haplotype2: ',differencehap2)
    
    Astrolabe.write('Sample: ')
    Astrolabe.write(sample + '\n')
    Astrolabe.write('\n')
    Astrolabe.write('HAPLOTYPE1' + '\n')
    Astrolabe.write('Haplotype1: ')
    Astrolabe.write(callhaplotypehap1 + '\n')
    Astrolabe.write('Shared SNPs: ',)
    i = 0
    for item in callhap1:
        i = i + 1
        Astrolabe.write(item)
        if i < len(callhap1):
            Astrolabe.write(',')
    Astrolabe.write('\n')
    Astrolabe.write('Match Score: ' + str(finalpercentmatchhap1) + '\n')
    Astrolabe.write('Sample Only Haplotype1: ')
    i = 0
    for item in differencehap1:
        i = i + 1
        Astrolabe.write(item)
        if i < len(differencehap1):
            Astrolabe.write(',')
    Astrolabe.write('\n')
    Astrolabe.write('\n')
    Astrolabe.write('HAPLOTYPE2' + '\n')
    Astrolabe.write('Haplotype2: ' + callhaplotypehap2 + '\n')
    Astrolabe.write('Shared SNPs: ')
    i = 0
    for item in callhap2:
        i = i + 1
        Astrolabe.write(item)
        if i < len(callhap2):
            Astrolabe.write(',')
    Astrolabe.write('\n')
    Astrolabe.write('Match Score: ' + str(finalpercentmatchhap2) + '\n')
    Astrolabe.write('Sample Only Haplotype2: ')
    i = 0
    for item in differencehap2:
        i = i + 1
        Astrolabe.write(item)
        if i < len(differencehap2):
            Astrolabe.write(',')