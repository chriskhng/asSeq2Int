## -
## - asSeq2Int
## -
## - Created by Chris Ng 20201214



#### TODO put Part 1 function below
#### Part 1 reformat the FASTA file into list of list for Part 2
#### It first opens the file
with open('ct_border.txt') as ct_border_file:
#### Splits the file into a list using "*/n>" as the delimiter
#### File can close now

#### "reverse compliment, " is removed

#### "/n" is replaced with ", " for all items in list

#### items in list is split into a list with ", " as the delimiter.