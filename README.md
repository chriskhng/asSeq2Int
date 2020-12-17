# asSeq2Int

asSeq2Int is a python-based code that takes sequences of interest (SoI) and proteins of interest (PoI) as inputs and outputs proteins that contains the SoI that interacts with the PoI.

## For CIBR final project submission
asSeq2Int will be incomplete at the time of submission with only 2 of the 6 main functions implemented.
The submitted parts will be able to take user inputs and output results as a .csv
(in the full code, it will output directly into the next part of the code as a list).

######Instructions for CIBR course instructors are included in the section below.

## Instructions (for CIBR final project testing)
The submitted code will take a amino acid sequence of interest as a user input.
It will then output a .csv that list proteins (included in the FASTA file) that contain your sequence of interest.


####Inputs
A dummy FASTA dataset is included in the repository for testing purposes. If you want to use a 
different FASTA, replace dummy1.FASTA with your .FASTA file name seen below in asSeq2Int.py:

```
with open('dummy1.FASTA') as FASTA_file:
```
######The full (post-CIBR) code will prompt the user for the file name when run. 

The amino acid sequence can be uppercase or lowercase. User can denote "any amino acid" with . , x, or X .

asSeq2Int.py pulled straight from the repo will currently look for "mxxt" as an SoI in dummy1.FASTA.

To use a different SoI, edit the user_input_SoI variable to any amino acid sequence of interest. 
```user_input_SoI = "mxxt"```

Sample amino acid sequences are included below with the number of sequence hits from the dummy1.FASTA shown.

####Running the code
#####To run the code:
```
./main.sh
```
This will run asSeq2Int.py, rename the output .csv to SeqHit-DATE-TIME.csv, and rsync it to the SeqHitResults directory.

If a larger FASTA is used, one may consider using HPC with SLURM.

#####To run the code with a SLURM scheduler for an HPC:
```
sbatch slurm.sh
```
This simply runs ./main.sh, and saves the CLI output to SeqHitReadOut.JobID.txt
The output .csv will still be renamed and rsync'ed to the SeqHitResults directory. 

####Sample Sequence of Interest input:
Number in brackets = number of hits in dummy1.FASTA
- SxSxSSXXSXSS (3)
- SxxTxxY (5)
- WxFxr (1)
- ExDxI (7)
- RxTxP (3)
- RRTYP (0)
- RxTkP (1)

The code should be able to take any sequence of interest. So feel free to test it out!

## Version log

1.0.0 Public Release with detailed README.md

0.6.0 Slurm scheduler support implemented. Run slurm.sh to use!

0.5.2 Bug fixed. Permissions edited for main.sh. rsync for the named output file works properly now. 

0.5.1 Dummy FASTA file for testing added to repository (erroneously omitted before)

0.5.0 main.sh launches asSep2Int.py, renames the output file as SeqHit(date-time).csv and rsyncs it to the result dir. 

0.4.0 Part 2 outputs temp_results.csv which lists proteins with the sequence of interest

0.3.0 Part 2 function implemented: list from Part 1 is searched for a code-defined SoI

0.2.0 Part 1 function implemented: FASTA file can be reformatted into a list for Part 2 

0.1.0 Initial Code Commit
