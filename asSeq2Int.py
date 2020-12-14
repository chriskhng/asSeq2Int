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
    #print(FASTAprotein)
    #print(FASTAprotein.find(','))
    FASTAproteinNames = FASTAprotein[0: FASTAprotein.find(',')]
    #print(FASTAproteinNames)
    proteinNamesSep = FASTAproteinNames.split(" ")


#### now we put out the protein sequence from the FASTA list
#### replaces all \n with ,
    FASTAprotein_comma = FASTAprotein.replace("\n", ", ")
#### replaces all '\",' with \&
    for_protein_seqjoin = FASTAprotein_comma.replace('\",', '*$')
    #for_protein_seqjoin = for_protein_seqjoin + "*"
    #print(for_protein_seqjoin.find("*$"))
    #print(for_protein_seqjoin[for_protein_seqjoin.find("*$")+3])
#### Saves sequence data into proteinSeqOnly starting from index of (*$ +3) to the last index
    proteinSeqOnly = for_protein_seqjoin[ for_protein_seqjoin.find("*$")+3: -1]
    print(proteinSeqOnly)


#### splits those items by ", " into list
    FASTAprotein_comma_split = FASTAprotein_comma.split(', ')
#### delete most unused items
    del FASTAprotein_comma_split[1:5]
    #print(FASTAprotein_comma_split)
    #print(for_protein_seqjoin)
    #print(unjoined_proteinseq)
    #for letter in FASTAprotein_comma_split:

#### joins the protein sequence into one item
    FASTAprotein_seqjoin = [FASTAprotein_comma_split[0], ''.join(FASTAprotein_comma_split[1:len(FASTAprotein_comma_split)])]
    lst_comma_raw_FASTA.append(FASTAprotein_comma_split)
    lst_trimmed_FASTA.append(FASTAprotein_seqjoin)






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