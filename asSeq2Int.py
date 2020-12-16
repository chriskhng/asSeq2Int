## -
## - asSeq2Int
## -
## - Created by Chris Ng 20201214

## - #### Initialize empty lists
lst_rawFASTA = []
proteinSeqOnly = []
lst_FASTAentry = []
lst_masterFASTA = []
lst_results = [['Protein Name', 'Sequence Hit', 'Position of Hit']]

## - #### Part 1

## - Part 1 reformat the FASTA file into list of list for Part 2
## - It first opens the file
with open('dummy1.FASTA') as FASTA_file:
    FASTA_data = FASTA_file.read()
## - File can close now

## - Splits the file into a list using "*/n>" as the delimiter
## - lst_rawFASTA is a list of each protein entry, containing protein name, sequence, etc, in a single string
lst_rawFASTA = FASTA_data.split('*\n>')

## - relevant info will be pulled out from each protein entry
## - We are interested in the protein name and protein sequence
for protein_entry in lst_rawFASTA:
## - The protein name is pulled from each FASTA entry and saved into FASTAproteinNames
## - This is done by indexing from 0 to the first comma (which delimits name from the next entry)
    FASTAproteinNames = protein_entry[0: protein_entry.find(',')]

## - Next, the protein sequence is pulled from protein_entry. Reformatting is required.
## - The protein sequence in protein_entry is seprated by "\n"
## - First, '\n' is replaced with ", "
    FASTAprotein_comma = protein_entry.replace("\n", ", ")
## - Next, the beginning of the protein sequence (and end of the previous item) is marked by '*$'
    for_protein_seqjoin = FASTAprotein_comma.replace('\",', '*$')
## - Then, only the string with sequence info is saved into proteinSeqOnly
## - This is done by indexing from where ("*$" is located + 3) till the end of the string
    proteinSeqOnly = for_protein_seqjoin[for_protein_seqjoin.find("*$")+3:]
## - Finally, the protein sequence is joined together by removing ', '
## - proteinSeqFinal is the protein sequence of each protein entry
    proteinSeqFinal = proteinSeqOnly.replace(', ', '')

## - Now, we put protein name and protein sequence together into a list for each entry
## - First, the protein names are separated into genomic name, common name, and ID name
    lst_FASTAentry = FASTAproteinNames.split(' ')
## - Next, the protein sequence is appended to end of the names.
    lst_FASTAentry.append (proteinSeqFinal)
## - Finally, the list for the entry is appended to the growing list of protein entries from the FASTA.
    lst_masterFASTA.append (lst_FASTAentry)


## - At this point, lst_masterFASTA contains artifacts from the reformatting above.
## - Namely, ">" and "*" remains on the first of first and last of last indices respectively.
## - These artifacts are removed in the following 2 lines.
(lst_masterFASTA[0])[0] = (lst_masterFASTA[0])[0].replace('>', '')
(lst_masterFASTA[-1])[-1] = (lst_masterFASTA[-1])[-1].replace('*', '')
print(lst_masterFASTA)

## - This list of sublists of protein entries will be used in Part 2.
## - This list will be searched for the user-input SoI to output the name of proteins containing the SoI


## - #### Part 2
## - Part 2 will search the lst_masterFASTA from Part 1 for the user-input SoI

## - Regular Expression (re) is imported and will be used for the search.
import re

######### NEEDS TO BE ACTUALLY user input at the end
user_input_SoI = "mxxt" #SxSXSSXXSXSS
## - the user input SoI will be .upper, in case user input in lowercase
upper_SoI = user_input_SoI.upper()
## - Then, if the user used x to denote "any", it will be replaced by .
regex_SoI = upper_SoI.replace("X", ".")
## - the reformated user-input is then placed into RegEx pattern match syntax
pattern = '^' + regex_SoI + "$"

## - The protein sequence in each protein entry in lst_masterFASTA will be iterated thru searching for SoI
for protein_entry in lst_masterFASTA:
## protein_entry looks like:
    #protein_entry = ['YAL001C', 'TFC3', 'SGDID:S000000001', 'MVLTIYPDELVQIVSDKI..."
    protein_seq = protein_entry[3]
## - The following cuts each protein sequence into blocks with the length of the input SoI
    for i in range(len(protein_seq)-(len(user_input_SoI)-1)):
        protein_sequence_block =protein_seq[i:(i + len(user_input_SoI))]
        # The following commented code checks to see if I cut the blocks correctly
        # print(protein_seq[i:(i+len(pattern)-2)])
        result = re.match(pattern, protein_sequence_block)
## - If a protein sequence block matches the user-input sequence, it will print:
        if result:
            print(upper_SoI + " found in:")
            print(protein_entry[1]) # the protein name and ...
            print("as " + protein_seq[i:(i + len(pattern) - 2)] + ' which starts at position: ' + str(i+1) + "\n")
            # The following appends to a list that will be used to populate the output .txt file
            lst_results.append([protein_entry[1], protein_seq[i:(i + len(pattern) - 2)], str(i+1)])
## - the actual sequence it matched, and which amino acid position the match started in the protein sequence
        else:
            continue

## - lst_results is then written into temp_results.csv with csv module
import csv
with open('temp_results.csv', 'w', newline='') as temp_results_file:
    writer = csv.writer(temp_results_file)
    writer.writerows(lst_results)

## - #### The .py code is over for the purposes of the CIBR final project
## - #### Next, temp_results.csv will be copied and renamed to the date-time.csv
## - #### Finally, this renamed csv will be rsynced
## - #### (currently set to a temp_dir in the current dir, but can be changed to a local dir).