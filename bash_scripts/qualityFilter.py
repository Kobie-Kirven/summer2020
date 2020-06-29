"""Quality filters the reads using BBDuk"""

import os

folderNames = ['initial', 'normal', 'experimental']
sampleIDs = [['I1','I2','I3'],['N2','N3','N4'],['E1','E3','E4','E5']]

path = "/Volumes/Elements/zebrafish_reads/"

num = 1
for i in range(len(folderNames)):
  for sample in sampleIDs[i]:
    os.system("bash bbmap/bbduk.sh in1="+ path + folderNames[i] + "/" + sample + "/" +sample+"_S"+ str(num) +"_L001_R1_001.fastq.gz in2="+ path + folderNames[i] + "/" + sample + "/" +sample+"_S"+ str(num) +"_L001_R2_001.fastq.gz out1="+ path +folderNames[i] + "/" + sample + "/" + sample + "_R1_filtered.fastq out2="+ path +folderNames[i] + "/" + sample + "/" + sample + "_R2_filtered.fastq ref=bbmap/resources/adapters.fa qtrim=r trimq=28 maq=28 minlen=30")
    num += 1
