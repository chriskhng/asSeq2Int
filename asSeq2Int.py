## -
## - asSeq2Int
## -
## - Created by Chris Ng 20201214

## - #### Initialize empty lists
lst_rawFASTA = []
lst_comma_raw_FASTA = []
lst_trimmed_FASTA = []
proteinSeqOnly = []
lst_FASTAentry = []
lst_masterFASTA = []

#### TODO put Part 1 function below
#### Part 1 reformat the FASTA file into list of list for Part 2
#### It first opens the file
with open('dummy1.FASTA') as FASTA_file:
    FASTA_data = FASTA_file.read()
#### File can close now
#### Splits the file into a list using "*/n>" as the delimiter
lst_rawFASTA = FASTA_data.split('*\n>')

for FASTAprotein in lst_rawFASTA:
#### we pull out the protein name from each FASTA entry
    FASTAproteinNames = FASTAprotein[0: FASTAprotein.find(',')]
    proteinNamesSep = FASTAproteinNames.split(" ")

#### now we put out the protein sequence from the FASTA list
#### replaces all \n with ,
    FASTAprotein_comma = FASTAprotein.replace("\n", ", ")
#### replaces all '\",' with \&
    for_protein_seqjoin = FASTAprotein_comma.replace('\",', '*$')
#### Saves sequence data into proteinSeqOnly starting from index of (*$ +3) to the last index
    proteinSeqOnly = for_protein_seqjoin[ for_protein_seqjoin.find("*$")+3:]
    proteinSeqFinal = proteinSeqOnly.replace(', ', '')
    lst_FASTAentry = FASTAproteinNames.split(' ')
    lst_FASTAentry.append (proteinSeqFinal)
    lst_masterFASTA.append (lst_FASTAentry)

# lst_masterFASTA is trimmed to rid of the > and * and the start and end (artifacts from the above reformatting)
(lst_masterFASTA[0])[0] = (lst_masterFASTA[0])[0].replace('>', '')
(lst_masterFASTA[-1])[-1] = (lst_masterFASTA[-1])[-1].replace('*', '')
print(lst_masterFASTA)
#print(FASTAmasterIndex0)
#lst_masterFASTA_untrimmed[1[1]].replace('>', '')
#print(lst_masterFASTA_untrimmed)








   # for line in FASTA_file
    #lst_rawFASTA = FASTA_file.split('*/n>')
    #for line in FASTA_file:
     #   print(line)


#### "reverse compliment, " is removed

#### "/n" is replaced with ", " for all items in list

#### items in list is split into a list with ", " as the delimiter.

#### TESTING lines
#print(lst_rawFASTA)
#print(lst_comma_raw_FASTA)
#print(FASTAprotein_seqjoin)
#print(lst_trimmed_FASTA)