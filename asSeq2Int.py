## -
## - asSeq2Int
## -
## - Created by Chris Ng 20201214

## - #### Initialize empty lists
lst_rawFASTA = []

#### TODO put Part 1 function below
#### Part 1 reformat the FASTA file into list of list for Part 2
#### It first opens the file
with open('dummy1.FASTA') as FASTA_file:
#### Splits the file into a list using "*/n>" as the delimiter
    FASTA_data = FASTA_file.read()
#print(FASTA_data)
lst_rawFASTA = FASTA_data.split('*\n>')


   # for line in FASTA_file
    #lst_rawFASTA = FASTA_file.split('*/n>')
    #for line in FASTA_file:
     #   print(line)

#### File can close now

#### "reverse compliment, " is removed

#### "/n" is replaced with ", " for all items in list

#### items in list is split into a list with ", " as the delimiter.

#### TESTING lines
print(lst_rawFASTA)