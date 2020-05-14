
## Analysis of Zebrafish data


##################
#BLAST+
##################
import os
from Bio import SeqIO

##Functions

##Get the input contigs sequences and IDS
#----'sample.fasta' is the file with contigs
ids, sequences = [],[]
for record in SeqIO.parse("sample.fasta", "fasta"):
    ids.append(record.id)
    sequences.append(record.seq)

##Begin the analysis pipeline
for i in range(len(ids)):
	flag = False
	##Put the queary sequence in a temporary file called "input.fasta"
	fn = open("input.fasta", "w")
	fn.write(">" + str(ids[i]) + "\n")
	fn.write(str(sequences[i]))
	flag = True

	##Preform the BLAST search on the query
	# blast("input.fasta")

	##Read the results from the BLAST output
	if flag == True:
		os.system("blastn -db nt -query input.fasta -out results.txt -remote")

 
# getch()